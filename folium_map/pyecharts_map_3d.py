from pyecharts import options as opts
from pyecharts.charts import Map3D
from pyecharts.globals import ChartType

example_data = [
    [[121.452369, 31.243339, 1000], [116.404188, 39.916016, 1000]],
    [[121.452369, 31.243339], [113.271429, 23.144109]],
    [[121.452369, 31.243339], [106.551538, 29.556681]],
    [[121.452369, 31.243339], [103.868704, 1.358448]],
    [[121.452369, 31.243339], [100.394541, 13.752482]],
    [[121.452369, 31.243339], [126.965321, 37.596048]],
    [[121.452369, 31.243339], [139.666576, 35.802312]],
    [[121.452369, 31.243339], [72.832377, 18.978547]],
    [[121.452369, 31.243339], [-78.695413, 37.488175]],
    [[121.452369, 31.243339], [-79.388071, 43.642058]],
    [[121.452369, 31.243339], [8.681552, 50.110366]],
    [[121.452369, 31.243339], [37.618172, 55.75696]],
    [[121.452369, 31.243339], [-0.119853, 51.503492]],
]
c = (
    Map3D(init_opts=opts.InitOpts(width="1800px", height="900px"))
    .add_schema(
        maptype="world",
        itemstyle_opts=opts.ItemStyleOpts(
            color="rgb(5,101,123)",
            opacity=1,
            border_width=0.8,
            border_color="rgb(62,215,213)",
        ),
        light_opts=opts.Map3DLightOpts(
            main_color="#fff",
            main_intensity=1.2,
            is_main_shadow=False,
            main_alpha=55,
            main_beta=10,
            ambient_intensity=0.3,
        ),
        view_control_opts=opts.Map3DViewControlOpts(center=[-10, 0, 10]),
        post_effect_opts=opts.Map3DPostEffectOpts(is_enable=False),
    )
    .add(
        series_name="",
        data_pair=example_data,
        type_=ChartType.LINES3D,
        effect=opts.Lines3DEffectOpts(
            is_show=True,
            period=4,
            trail_width=3,
            trail_length=0.5,
            trail_color="#f00",
            trail_opacity=1,
        ),
        linestyle_opts=opts.LineStyleOpts(is_show=False, color="#fff", opacity=0),
    )
    .set_global_opts(
        title_opts=opts.TitleOpts(title="Map3D-Lines3D"),
        visualmap_opts=opts.VisualMapOpts(is_show=False),
        tooltip_opts=opts.TooltipOpts(is_show=True),
    )
    .render("map3d_with_lines3d.html")
)
