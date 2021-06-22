from django.shortcuts import redirect
from django.http import HttpResponse
from django.template import loader
from django.db.models import Q
from pyecharts.charts import Bar, Line
from pyecharts import options as opts
from pyecharts.globals import ThemeType
from pathlib import Path
import os

from .models import AuthorPaperCount


BASE_DIR = Path(__file__).resolve().parent.parent.parent
cvpr_list = [471, 540, 602, 643, 783, 979, 1109, 1466, None]
iccv_list = [454, None, 526, None, 621, None, 1075, None, None]
wacv_list = [None, None, None, None, None, None, None, 378, 406]


def author_ranking(request, conf, year):
    if not request.session.get('is_login', None):
        return redirect('/home')
    
    request.session['search_by'] = 'all'
    request.session['search'] = ''
    template = loader.get_template(os.path.join(BASE_DIR, 'templates/statistics/author-ranking.html'))
    bar_chart = bar_base(conf, year)
    context = dict(
        echart = bar_chart.render_embed()
    )
    return HttpResponse(template.render(context, request))


def paper_statistics(request):
    if not request.session.get('is_login', None):
        return redirect('/home')
    
    template = loader.get_template(os.path.join(BASE_DIR, 'templates/statistics/paper-statistics.html'))
    line_chart = line_base(cvpr_list, iccv_list, wacv_list)
    context = dict(
        echart = line_chart.render_embed()
    )
    return HttpResponse(template.render(context, request))


def get_author_ranking(conf, year):
    author_counts = AuthorPaperCount.objects.filter(
        Q(conference=conf), Q(year=year)
    )
    author_list = [author_count.author for author_count in author_counts]
    count_list = [author_count.count for author_count in author_counts]
    return author_list, count_list


def bar_base(conf, year) -> Bar:
    author_list, count_list = get_author_ranking(conf, year)

    bar_chart = (
        Bar(init_opts=opts.InitOpts(width='100%', height='80%', theme=ThemeType.MACARONS))
        .add_xaxis(author_list)
        .add_yaxis(conf.upper()+str(year), count_list, color='purple')
        .set_global_opts(
            title_opts=opts.TitleOpts(title="Author Ranking Chart"),
            xaxis_opts=opts.AxisOpts(axislabel_opts={"rotate":20}),
            yaxis_opts=opts.AxisOpts(max_=count_list[0]),
            datazoom_opts=opts.DataZoomOpts(
                type_='inside',
                range_start=None, range_end=None,
                start_value=author_list[0], end_value=author_list[9], is_zoom_lock=True,
            ),
            toolbox_opts=opts.ToolboxOpts(
                feature=opts.ToolBoxFeatureOpts(data_view=None, data_zoom=None, brush=None)
            )
        )
    )
    return bar_chart


def line_base(cvpr_list, iccv_list, wacv_list) -> Line:
    line_chart = (
        Line(init_opts=opts.InitOpts(width='100%', height='80%', theme=ThemeType.MACARONS))
        .add_xaxis(xaxis_data=list(map(str, list(range(2013, 2022)))))
        .add_yaxis('CVPR', cvpr_list, is_connect_nones=True)
        .add_yaxis('ICCV', iccv_list, is_connect_nones=True)
        .add_yaxis('WACV', wacv_list, is_connect_nones=True)
        .set_global_opts(
            title_opts=opts.TitleOpts(title="Paper Statistics Chart"),
            toolbox_opts=opts.ToolboxOpts(
                feature=opts.ToolBoxFeatureOpts(data_view=None, data_zoom=None, brush=None)
            )
        )
    )
    return line_chart
