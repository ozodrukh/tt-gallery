from yt_dlp.update import version_tuple
from yt_dlp.version import __version__

if version_tuple(__version__) < (2023, 9, 24):
    raise ImportError('yt-dlp version 2023.09.24 or later is required to use the TTUser plugin')

from yt_dlp.extractor.tiktok import TikTokIE

class TikTokGalleryIE(TikTokIE, plugin_name="TTGalery"):
    def _parse_aweme_video_app(self, aweme_detail):
        extracted = super()._parse_aweme_video_app(aweme_detail)
        tt_gallery_slides = aweme_detail['image_post_info']['images']

        if len(tt_gallery_slides) > 0:
            gallery = []
            for slide in tt_gallery_slides:
                gallery.append({
                    'url': slide['display_image']['url_list'][-1],
                    'width': slide['display_image']['width'],
                    'height': slide['display_image']['height']
                })

            extracted.update({
                'gallery_post': gallery,
            })
        
        return extracted
        # return 

__all__ = []