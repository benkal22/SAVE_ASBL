from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.utils.translation import gettext_lazy as _
from .models import CarouselPluginModel, SlidePluginModel, VideoIntro, Engagement, Result, Testimonial, News

@plugin_pool.register_plugin
class CustomCarouselPlugin(CMSPluginBase):
    model = CarouselPluginModel
    name = _("Custom Carousel")
    render_template = "cms_plugins/carousel_plugin.html"
    allow_children = True  # Permet d'ajouter des éléments enfants (les slides)
    child_classes = ["CustomSlidePlugin"]

    def render(self, context, instance, placeholder):
        context = super().render(context, instance, placeholder)
        return context

@plugin_pool.register_plugin
class CustomSlidePlugin(CMSPluginBase):
    model = SlidePluginModel
    name = _("Custom Slide")
    render_template = "cms_plugins/slide_plugin.html"
    require_parent = True  # Ce plugin doit être un enfant d'un autre plugin
    parent_classes = ['CustomCarouselPlugin']

    def render(self, context, instance, placeholder):
        context = super().render(context, instance, placeholder)
        context['instance'] = instance
        return context

@plugin_pool.register_plugin
class VideoIntroPlugin(CMSPluginBase):
    model = VideoIntro
    render_template = "cms_plugins/video_intro.html"
    cache = False

@plugin_pool.register_plugin
class EngagementPlugin(CMSPluginBase):
    model = Engagement
    render_template = "cms_plugins/engagements.html"
    cache = False

@plugin_pool.register_plugin
class ResultPlugin(CMSPluginBase):
    model = Result
    render_template = "cms_plugins/results.html"
    cache = False

@plugin_pool.register_plugin
class TestimonialPlugin(CMSPluginBase):
    model = Testimonial
    render_template = "cms_plugins/testimonials.html"
    cache = False

@plugin_pool.register_plugin
class NewsPlugin(CMSPluginBase):
    model = News
    render_template = "cms_plugins/news.html"
    cache = False