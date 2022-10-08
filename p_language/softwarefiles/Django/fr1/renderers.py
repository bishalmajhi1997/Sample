from rest_framework import renderers
class UserRenderer(renderers.JSONRenderer):
    def render(self,data,accepted_media_type=None,renderer_context=None):
        response=""
        import pdb
        pdb.set_trace()
        return super().render(data,accepted_media_type=accepted_media_type,renderer_context=renderer_context)
