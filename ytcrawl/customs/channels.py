"""
list(part, hl=None, mine=None, mySubscribers=None, id=None, managedByMe=None, onBehalfOfContentOwner=None, forUsername=None, pageToken=None, categoryId=None, maxResults=None)
Returns a collection of zero or more channel resources that match the request criteria.

Args:
  part: string, The part parameter specifies a comma-separated list of one or more channel resource properties that the API response will include.
  [id, snippet, brandingSettings, contentDetails, invideoPromotion, statistics, topicDetails]

If the parameter identifies a property that contains child properties, the child properties will be included in the response. For example, in a channel resource, the contentDetails property contains other properties, such as the uploads properties. As such, if you set part=contentDetails, the API response will also contain all of those nested properties. (required)
  hl: string, The hl parameter should be used for filter out the properties that are not in the given language. Used for the brandingSettings part.
  mine: boolean, Set this parameter's value to true to instruct the API to only return channels owned by the authenticated user.
  mySubscribers: boolean, Use the subscriptions.list method and its mySubscribers parameter to retrieve a list of subscribers to the authenticated user's channel.
  id: string, The id parameter specifies a comma-separated list of the YouTube channel ID(s) for the resource(s) that are being retrieved. In a channel resource, the id property specifies the channel's YouTube channel ID.
  managedByMe: boolean, Note: This parameter is intended exclusively for YouTube content partners.

Set this parameter's value to true to instruct the API to only return channels managed by the content owner that the onBehalfOfContentOwner parameter specifies. The user must be authenticated as a CMS account linked to the specified content owner and onBehalfOfContentOwner must be provided.
  onBehalfOfContentOwner: string, Note: This parameter is intended exclusively for YouTube content partners.

The onBehalfOfContentOwner parameter indicates that the request's authorization credentials identify a YouTube CMS user who is acting on behalf of the content owner specified in the parameter value. This parameter is intended for YouTube content partners that own and manage many different YouTube channels. It allows content owners to authenticate once and get access to all their video and channel data, without having to provide authentication credentials for each individual channel. The CMS account that the user authenticates with must be linked to the specified YouTube content owner.
  forUsername: string, The forUsername parameter specifies a YouTube username, thereby requesting the channel associated with that username.
  pageToken: string, The pageToken parameter identifies a specific page in the result set that should be returned. In an API response, the nextPageToken and prevPageToken properties identify other pages that could be retrieved.
  categoryId: string, The categoryId parameter specifies a YouTube guide category, thereby requesting YouTube channels associated with that category.
  maxResults: integer, The maxResults parameter specifies the maximum number of items that should be returned in the result set.

Returns:
  An object of the form:

    {
    "eventId": "A String", # Serialized EventId of the request which produced this response.
    "nextPageToken": "A String", # The token that can be used as the value of the pageToken parameter to retrieve the next page in the result set.
    "kind": "youtube#channelListResponse", # Identifies what kind of resource this is. Value: the fixed string "youtube#channelListResponse".
    "visitorId": "A String", # The visitorId identifies the visitor.
    "items": [ # A list of channels that match the request criteria.
      { # A channel resource contains information about a YouTube channel.
        "status": { # JSON template for the status part of a channel. # The status object encapsulates information about the privacy status of the channel.
          "privacyStatus": "A String", # Privacy status of the channel.
          "isLinked": True or False, # If true, then the user is linked to either a YouTube username or G+ account. Otherwise, the user doesn't have a public YouTube identity.
          "longUploadsStatus": "A String", # The long uploads status of this channel. See
        },
        "invideoPromotion": { # Describes an invideo promotion campaign consisting of multiple promoted items. A campaign belongs to a single channel_id. # The invideoPromotion object encapsulates information about promotion campaign associated with the channel.
          "defaultTiming": { # Describes a temporal position of a visual widget inside a video. # The default temporal position within the video where the promoted item will be displayed. Can be overriden by more specific timing in the item.
            "offsetMs": "A String", # Defines the time at which the promotion will appear. Depending on the value of type the value of the offsetMs field will represent a time offset from the start or from the end of the video, expressed in milliseconds.
            "type": "A String", # Describes a timing type. If the value is offsetFromStart, then the offsetMs field represents an offset from the start of the video. If the value is offsetFromEnd, then the offsetMs field represents an offset from the end of the video.
            "durationMs": "A String", # Defines the duration in milliseconds for which the promotion should be displayed. If missing, the client should use the default.
          },
          "items": [ # List of promoted items in decreasing priority.
            { # Describes a single promoted item.
              "timing": { # Describes a temporal position of a visual widget inside a video. # The temporal position within the video where the promoted item will be displayed. If present, it overrides the default timing.
                "offsetMs": "A String", # Defines the time at which the promotion will appear. Depending on the value of type the value of the offsetMs field will represent a time offset from the start or from the end of the video, expressed in milliseconds.
                "type": "A String", # Describes a timing type. If the value is offsetFromStart, then the offsetMs field represents an offset from the start of the video. If the value is offsetFromEnd, then the offsetMs field represents an offset from the end of the video.
                "durationMs": "A String", # Defines the duration in milliseconds for which the promotion should be displayed. If missing, the client should use the default.
              },
              "promotedByContentOwner": True or False, # If true, the content owner's name will be used when displaying the promotion. This field can only be set when the update is made on behalf of the content owner.
              "customMessage": "A String", # A custom message to display for this promotion. This field is currently ignored unless the promoted item is a website.
              "id": { # Describes a single promoted item id. It is a union of various possible types. # Identifies the promoted item.
                "websiteUrl": "A String", # If the promoted item represents a website, this field represents the url pointing to the website. This field will be present only if type has the value website.
                "recentlyUploadedBy": "A String", # If type is recentUpload, this field identifies the channel from which to take the recent upload. If missing, the channel is assumed to be the same channel for which the invideoPromotion is set.
                "type": "A String", # Describes the type of the promoted item.
                "videoId": "A String", # If the promoted item represents a video, this field represents the unique YouTube ID identifying it. This field will be present only if type has the value video.
              },
            },
          ],
          "useSmartTiming": True or False, # Indicates whether the channel's promotional campaign uses "smart timing." This feature attempts to show promotions at a point in the video when they are more likely to be clicked and less likely to disrupt the viewing experience. This feature also picks up a single promotion to show on each video.
          "position": { # Describes the spatial position of a visual widget inside a video. It is a union of various position types, out of which only will be set one. # The spatial position within the video where the promoted item will be displayed.
            "cornerPosition": "A String", # Describes in which corner of the video the visual widget will appear.
            "type": "A String", # Defines the position type.
          },
        },
        "kind": "youtube#channel", # Identifies what kind of resource this is. Value: the fixed string "youtube#channel".
        "statistics": { # Statistics about a channel: number of subscribers, number of videos in the channel, etc. # The statistics object encapsulates statistics for the channel.
          "commentCount": "A String", # The number of comments for the channel.
          "subscriberCount": "A String", # The number of subscribers that the channel has.
          "videoCount": "A String", # The number of videos uploaded to the channel.
          "hiddenSubscriberCount": True or False, # Whether or not the number of subscribers is shown for this user.
          "viewCount": "A String", # The number of times the channel has been viewed.
        },
        "contentOwnerDetails": { # The contentOwnerDetails object encapsulates channel data that is relevant for YouTube Partners linked with the channel. # The contentOwnerDetails object encapsulates channel data that is relevant for YouTube Partners linked with the channel.
          "contentOwner": "A String", # The ID of the content owner linked to the channel.
          "timeLinked": "A String", # The date and time of when the channel was linked to the content owner. The value is specified in ISO 8601 (YYYY-MM-DDThh:mm:ss.sZ) format.
        },
        "topicDetails": { # Freebase topic information related to the channel. # The topicDetails object encapsulates information about Freebase topics associated with the channel.
          "topicIds": [ # A list of Freebase topic IDs associated with the channel. You can retrieve information about each topic using the Freebase Topic API.
            "A String",
          ],
          "topicCategories": [ # A list of Wikipedia URLs that describe the channel's content.
            "A String",
          ],
        },
        "contentDetails": { # Details about the content of a channel. # The contentDetails object encapsulates information about the channel's content.
          "relatedPlaylists": {
            "watchLater": "A String", # The ID of the playlist that contains the channel"s watch later playlist. Use the playlistItems.insert and  playlistItems.delete to add or remove items from that list.
            "watchHistory": "A String", # The ID of the playlist that contains the channel"s watch history. Use the  playlistItems.insert and  playlistItems.delete to add or remove items from that list.
            "likes": "A String", # The ID of the playlist that contains the channel"s liked videos. Use the   playlistItems.insert and  playlistItems.delete to add or remove items from that list.
            "favorites": "A String", # The ID of the playlist that contains the channel"s favorite videos. Use the  playlistItems.insert and  playlistItems.delete to add or remove items from that list.
            "uploads": "A String", # The ID of the playlist that contains the channel"s uploaded videos. Use the  videos.insert method to upload new videos and the videos.delete method to delete previously uploaded videos.
          },
        },
        "brandingSettings": { # Branding properties of a YouTube channel. # The brandingSettings object encapsulates information about the branding of the channel.
          "image": { # Branding properties for images associated with the channel. # Branding properties for branding images.
            "largeBrandedBannerImageImapScript": { # The image map script for the large banner image.
              "default": "A String",
              "localized": [
                {
                  "value": "A String",
                  "language": "A String",
                },
              ],
              "defaultLanguage": { # The language of the default property.
                "value": "A String",
              },
            },
            "smallBrandedBannerImageUrl": { # The URL for the 640px by 70px banner image that appears below the video player in the default view of the video watch page.
              "default": "A String",
              "localized": [
                {
                  "value": "A String",
                  "language": "A String",
                },
              ],
              "defaultLanguage": { # The language of the default property.
                "value": "A String",
              },
            },
            "bannerTvImageUrl": "A String", # Banner image. TV size extra high resolution (2120x1192).
            "bannerTvLowImageUrl": "A String", # Banner image. TV size low resolution (854x480).
            "largeBrandedBannerImageUrl": { # The URL for the 854px by 70px image that appears below the video player in the expanded video view of the video watch page.
              "default": "A String",
              "localized": [
                {
                  "value": "A String",
                  "language": "A String",
                },
              ],
              "defaultLanguage": { # The language of the default property.
                "value": "A String",
              },
            },
            "bannerImageUrl": "A String", # Banner image. Desktop size (1060x175).
            "backgroundImageUrl": { # The URL for the background image shown on the video watch page. The image should be 1200px by 615px, with a maximum file size of 128k.
              "default": "A String",
              "localized": [
                {
                  "value": "A String",
                  "language": "A String",
                },
              ],
              "defaultLanguage": { # The language of the default property.
                "value": "A String",
              },
            },
            "smallBrandedBannerImageImapScript": { # The image map script for the small banner image.
              "default": "A String",
              "localized": [
                {
                  "value": "A String",
                  "language": "A String",
                },
              ],
              "defaultLanguage": { # The language of the default property.
                "value": "A String",
              },
            },
            "bannerExternalUrl": "A String", # This is used only in update requests; if it's set, we use this URL to generate all of the above banner URLs.
            "watchIconImageUrl": "A String", # The URL for the image that appears above the top-left corner of the video player. This is a 25-pixel-high image with a flexible width that cannot exceed 170 pixels.
            "bannerTvMediumImageUrl": "A String", # Banner image. TV size medium resolution (1280x720).
            "bannerMobileImageUrl": "A String", # Banner image. Mobile size (640x175).
            "bannerTabletHdImageUrl": "A String", # Banner image. Tablet size high resolution (2276x377).
            "bannerTvHighImageUrl": "A String", # Banner image. TV size high resolution (1920x1080).
            "trackingImageUrl": "A String", # The URL for a 1px by 1px tracking pixel that can be used to collect statistics for views of the channel or video pages.
            "bannerTabletLowImageUrl": "A String", # Banner image. Tablet size low resolution (1138x188).
            "bannerMobileExtraHdImageUrl": "A String", # Banner image. Mobile size high resolution (1440x395).
            "bannerTabletImageUrl": "A String", # Banner image. Tablet size (1707x283).
            "bannerMobileLowImageUrl": "A String", # Banner image. Mobile size low resolution (320x88).
            "bannerMobileMediumHdImageUrl": "A String", # Banner image. Mobile size medium/high resolution (960x263).
            "bannerTabletExtraHdImageUrl": "A String", # Banner image. Tablet size extra high resolution (2560x424).
            "bannerMobileHdImageUrl": "A String", # Banner image. Mobile size high resolution (1280x360).
          },
          "watch": { # Branding properties for the watch. All deprecated. # Branding properties for the watch page.
            "textColor": "A String", # The background color for the video watch page's branded area.
            "featuredPlaylistId": "A String", # An ID that uniquely identifies a playlist that displays next to the video player.
            "backgroundColor": "A String", # The text color for the video watch page's branded area.
          },
          "channel": { # Branding properties for the channel view. # Branding properties for the channel view.
            "description": "A String", # Specifies the channel description.
            "title": "A String", # Specifies the channel title.
            "country": "A String", # The country of the channel.
            "showBrowseView": True or False, # Whether the tab to browse the videos should be displayed.
            "featuredChannelsTitle": "A String", # Title for the featured channels tab.
            "defaultLanguage": "A String",
            "unsubscribedTrailer": "A String", # The trailer of the channel, for users that are not subscribers.
            "keywords": "A String", # Lists keywords associated with the channel, comma-separated.
            "profileColor": "A String", # A prominent color that can be rendered on this channel page.
            "defaultTab": "A String", # Which content tab users should see when viewing the channel.
            "moderateComments": True or False, # Whether user-submitted comments left on the channel page need to be approved by the channel owner to be publicly visible.
            "featuredChannelsUrls": [ # The list of featured channels.
              "A String",
            ],
            "trackingAnalyticsAccountId": "A String", # The ID for a Google Analytics account to track and measure traffic to the channels.
            "showRelatedChannels": True or False, # Whether related channels should be proposed.
          },
          "hints": [ # Additional experimental branding properties.
            { # A pair Property / Value.
              "property": "A String", # A property.
              "value": "A String", # The property's value.
            },
          ],
        },
        "conversionPings": { # The conversionPings object encapsulates information about conversion pings that need to be respected by the channel. # The conversionPings object encapsulates information about conversion pings that need to be respected by the channel.
          "pings": [ # Pings that the app shall fire (authenticated by biscotti cookie). Each ping has a context, in which the app must fire the ping, and a url identifying the ping.
            { # Pings that the app shall fire (authenticated by biscotti cookie). Each ping has a context, in which the app must fire the ping, and a url identifying the ping.
              "conversionUrl": "A String", # The url (without the schema) that the player shall send the ping to. It's at caller's descretion to decide which schema to use (http vs https) Example of a returned url: //googleads.g.doubleclick.net/pagead/ viewthroughconversion/962985656/?data=path%3DtHe_path%3Btype%3D cview%3Butuid%3DGISQtTNGYqaYl4sKxoVvKA&labe=default The caller must append biscotti authentication (ms param in case of mobile, for example) to this ping.
              "context": "A String", # Defines the context of the ping.
            },
          ],
        },
        "snippet": { # Basic details about a channel, including title, description and thumbnails. # The snippet object contains basic details about the channel, such as its title, description, and thumbnail images.
          "description": "A String", # The description of the channel.
          "title": "A String", # The channel's title.
          "country": "A String", # The country of the channel.
          "customUrl": "A String", # The custom url of the channel.
          "publishedAt": "A String", # The date and time that the channel was created. The value is specified in ISO 8601 (YYYY-MM-DDThh:mm:ss.sZ) format.
          "defaultLanguage": "A String", # The language of the channel's default title and description.
          "localized": { # Channel localization setting # Localized title and description, read-only.
            "description": "A String", # The localized strings for channel's description.
            "title": "A String", # The localized strings for channel's title.
          },
          "thumbnails": { # Internal representation of thumbnails for a YouTube resource. # A map of thumbnail images associated with the channel. For each object in the map, the key is the name of the thumbnail image, and the value is an object that contains other information about the thumbnail.
              #
              # When displaying thumbnails in your application, make sure that your code uses the image URLs exactly as they are returned in API responses. For example, your application should not use the http domain instead of the https domain in a URL returned in an API response.
              #
              # Beginning in July 2018, channel thumbnail URLs will only be available in the https domain, which is how the URLs appear in API responses. After that time, you might see broken images in your application if it tries to load YouTube images from the http domain.
            "default": { # A thumbnail is an image representing a YouTube resource. # The default image for this resource.
              "url": "A String", # The thumbnail image's URL.
              "width": 42, # (Optional) Width of the thumbnail image.
              "height": 42, # (Optional) Height of the thumbnail image.
            },
            "high": { # A thumbnail is an image representing a YouTube resource. # The high quality image for this resource.
              "url": "A String", # The thumbnail image's URL.
              "width": 42, # (Optional) Width of the thumbnail image.
              "height": 42, # (Optional) Height of the thumbnail image.
            },
            "medium": { # A thumbnail is an image representing a YouTube resource. # The medium quality image for this resource.
              "url": "A String", # The thumbnail image's URL.
              "width": 42, # (Optional) Width of the thumbnail image.
              "height": 42, # (Optional) Height of the thumbnail image.
            },
            "maxres": { # A thumbnail is an image representing a YouTube resource. # The maximum resolution quality image for this resource.
              "url": "A String", # The thumbnail image's URL.
              "width": 42, # (Optional) Width of the thumbnail image.
              "height": 42, # (Optional) Height of the thumbnail image.
            },
            "standard": { # A thumbnail is an image representing a YouTube resource. # The standard quality image for this resource.
              "url": "A String", # The thumbnail image's URL.
              "width": 42, # (Optional) Width of the thumbnail image.
              "height": 42, # (Optional) Height of the thumbnail image.
            },
          },
        },
        "auditDetails": { # The auditDetails object encapsulates channel data that is relevant for YouTube Partners during the audit process. # The auditionDetails object encapsulates channel data that is relevant for YouTube Partners during the audition process.
          "communityGuidelinesGoodStanding": True or False, # Whether or not the channel respects the community guidelines.
          "contentIdClaimsGoodStanding": True or False, # Whether or not the channel has any unresolved claims.
          "copyrightStrikesGoodStanding": True or False, # Whether or not the channel has any copyright strikes.
        },
        "etag": "A String", # Etag of this resource.
        "id": "A String", # The ID that YouTube uses to uniquely identify the channel.
        "localizations": { # Localizations for different languages
          "a_key": { # Channel localization setting # The language tag, using string since map_key require simple types.
            "description": "A String", # The localized strings for channel's description.
            "title": "A String", # The localized strings for channel's title.
          },
        },
      },
    ],
    "tokenPagination": { # Stub token pagination template to suppress results.
    },
    "etag": "A String", # Etag of this resource.
    "prevPageToken": "A String", # The token that can be used as the value of the pageToken parameter to retrieve the previous page in the result set.
    "pageInfo": { # Paging details for lists of resources, including total number of items available and number of resources returned in a single page.
      "totalResults": 42, # The total number of results in the result set.
      "resultsPerPage": 42, # The number of results included in the API response.
    },
  }
  """

#!/usr/bin/python

# This sample executes a search request for the specified search term.
# Sample usage:
#   python search.py --q=surfing --max-results=10
# NOTE: To use the sample, you must provide a developer key obtained
#       in the Google APIs Console. Search for "REPLACE_ME" in this code
#       to find the correct place to provide that key..

import argparse

from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

import json
import os

# Set DEVELOPER_KEY to the API key value from the APIs & auth > Registered apps
# tab of
#   https://cloud.google.com/console
# Please ensure that you have enabled the YouTube Data API for your project.
DEVELOPER_KEY = 'AIzaSyCVMEUGxxsSw-BKH4c06PHKr_F4qjSdwJw'
YOUTUBE_API_SERVICE_NAME = 'youtube'
YOUTUBE_API_VERSION = 'v3'


def youtube_channels(options=None):
    youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,
                    developerKey=options.api_key if options.api_key else DEVELOPER_KEY)

    # Call the search.list method to retrieve results matching the specified
    # query term.
    response = youtube.channels().list(
        part='statistics, brandingSettings, snippet',
        hl=None,
        mine=None,
        mySubscribers=None,
        id=options.channel_id,
        # id='UCP7jMXSY2xbc3KCAE0MHQ',
        managedByMe=None,
        onBehalfOfContentOwner=None,
        forUsername=None,
        # forUsername='lexfridman',
        pageToken=None,
        categoryId=None,
        maxResults=None,
        # fields='items(statistics(subscriberCount))'
        fields="items(statistics(commentCount, subscriberCount, videoCount, viewCount), brandingSettings(channel(description, title, country, defaultLanguage, keywords)), snippet(publishedAt))"
        # fields='items(id,brandingSettings(channel(title,description,country,keywords)),snippet(publishedAt,defaultLanguage),statistics(commentCount,subscriberCount,videoCount,viewCount))'
    ).execute()

    # Add each result to the appropriate list, and then display the lists of
    # matching videos, channels, and playlists.
    # print(response.get('items', []))
    # for result in response.get('items', []):
    #     print('\nChannel title:', result['snippet']['channelTitle'], '\nTitle: ',
    #           result['snippet']['title'], '\nDescription: ', result['snippet']['description'])
    return response

# Two Minute Papers: UCbfYPyITQ-7l4upoX8nvctg
# lexfridman: UCSHZKyawb77ixDdsGog4iWA
# Henry AI Labs: UCHB9VepY6kYvZjj0Bgxnpbw
# kaggledotcom: UCSNeZleDn9c74yQc-EKnVTA
# Arxiv Insights: UCNIkB2IeJ-6AmZv7bQ1oBYg
# Yannic Kilcher: UCZHmQk67mSJgfCCTn7xBfew
# Leo Isikdogan: UC-YAxUbpa1hvRyfJBKFNcJA

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    # parser.add_argument('--q', help='Search term', default='Google')
    # parser.add_argument('--max-results', help='Max results', default=50)
    # parser.add_argument('--region-code', help='Region code', default=None)
    # parser.add_argument('--page-token', help='Page token', default=None)
    # parser.add_argument('--order', help='Order', default=None)
    args = parser.parse_args()

    # try:
    #     youtube_channels(args)
    # except (HttpError, e):
    #     print('An HTTP error %d occurred:\n%s' % (e.resp.status, e.content))
    if type(args.list_channel_ids) == str:
        with open(args.list_channel_ids) as f:
            args.list_channel_ids = json.load(f)[0].values()
    for channel_id in args.list_channel_ids:
        args.channel_id = channel_id
        response = youtube_channels(args)

    print(response)