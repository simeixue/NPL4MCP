# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/mcp-metricool/src/mcp_metricool/tools/tools.py
# module: src.mcp_metricool.tools.tools
# qname: src.mcp_metricool.tools.tools.update_schedule_post
# lines: 618-685
async def update_schedule_post(id: str, date:str, blog_id: int, info: json) -> str | dict[str, Any]:
    """
    Update a scheduled post in Metricool. You need the id of the post to update. Get it from the get_scheduled_posts tool previous on the conversation.
    Ask the user if they're sure they want to modify the post, including what will be changed, and require them to confirm.
    Do not retry if there is a problem.
    To update the post, ensure the full original content is included in the request, modifying only the new information while keeping the rest unchanged and maintaining the original structure.
    If the post include Instagram, is a must to have at least one image or video. Posts must include an image or a carousel, Reels must include a video, and Stories can include either an image or a video. If you don't have more information, you can ask the user about it and wait until you have the information.
    If the post include Pinterest, is a must to have a image and the board where to publish the pin. If you don't have more information, you can ask the user about it and wait until you have the information.
    If the post include Youtube, is a must to have a video, select the audience (if it's video made for kids or not) and the title of the video. If you don't have more information, you can ask the user about it and wait until you have the information.
    If the post include Tiktok, is a must to have at least one image or video. If you don't have more information, you can ask the user about it and wait until you have the information.
    If the post is Facebook Reel, is a must to have a video. If is Facebook Story, image or video is needed. If you don't have more information, you can ask the user about it and wait until you have the information.
    If the post is Bluesky, make sure the text does not exceed 300 characters. If the content exceeds that limit, do not retry and return an error informing the user: "Error: The text exceeds the 300-character limit allowed on Bluesky. Please edit it."
    If the post is for X (formerly Twitter), make sure before posting that the text does not exceed 280 characters. You must NOT split the message into multiple tweets or threads, the message must be evaluated strictly against a 280-character limit. If the text exceeds 280 characters, do not retry and return only the following error message and stop processing:

    The date can't be in the past.

    Args:
     date: Date and time to publish the post. The format is YYYY-MM-DDT00:00:00
     id: id of the post to update. Get it from the get_scheduled_posts tool previous on the conversation.
     blog id: Blog id of the Metricool brand account.
     info: Data of the post to be scheduled. Should be a json object with the following fields:
        id: id of the post to update. Get it from the get_scheduled_posts tool previous on the conversation. The format is "id":<integer>
        uuid: uuid of the post to update. Get it from the get_scheduled_posts tool previous on the conversation. The format is "uuid":"<string>"
        autoPublish: True or False, default is True.
        descendants: list with the args of the other posts if it is a thread with the format [args of the second post, args of the third post,...  ], default is empty list if there is no thread.
        draft: True or False, default is False.
        firstCommentText: Text of the first comment of the post. Default ""
        hasNotReadNotes: True or False, default is False.
        media: default is empty list.
        mediaAltText: default is empty list.
        providers: always need at least one provider with the format [{"network":"<string>"}]. Use "twitter" for X posts.
        publicationDate: Date and timezone of the post. The format is {dateTime:"2025-01-01T00:00:00", timezone:"Europe/Madrid"}
        shortener: True or False, default is False.
        smartLinkData: default is {ids:[]}
        text: Text of the post.
        Always you need to add the networkData for the posts, as empty if you don't have more information. Only include the networkData for the networks you have in the providers list.
            The format is "twitterData": {"tags":[]}, Tags is used for tagging people on the images of the post, not hashtags.
                            "facebookData": {"type":"<string>", "title":"<string>", "boost":<double>, "boostPayer":"<string>", "boostBeneficiary":"<string>"},
                                Facebook type can be "POST", "REEL" or "STORY"
                                Facebook title is only available for Facebook videos (This is separate from the main text of the post).
                                Facebook boost, boostPayer, and boostBeneficiary are only included if they are promoted posts.
                            "instagramData": {"type": "<string>" (default = POST), "collaborators":[{username: "string", deleted: false}]], "carouselTags":{"<number>":[{"username":"<string>","x":<double>,"y":<double>}]} (number is the index of the image within the carousel), "showReelOnFeed": "<boolean>" (default = true), "boost":<double>, "boostPayer":"<string>", "boostBeneficiary":"<string>"},
                                Instagram type can be "POST", "REEL" or "STORY".
                                There could be more than one collaborator, following the same structure.
                                The carouselTags is a dictionary with the number of the image in the carousel as key and a list of tags for that image.
                            "linkedinData": {"documentTitle": "<string>", "publishImagesAsPDF": "<boolean>" (default = false), "previewIncluded": "<boolean>" (default = true), "type": "<string>" (default = post), "poll": {"question": "<string>", "options": [{"text": "<string>"}, {"text": "<string>"}], "settings": {"duration": "<string>"}}},
                                Linkedin type can be "post" or "poll".
                                If there is a documentTitle in Linkedin, publishImagesAsPDF must be true.
                                Linkedin poll duration can be "ONE_DAY", "THREE_DAYS", "SEVEN_DAYS " or "FOURTEEN_DAYS ".
                            "pinterestData": {"boardId":"<string>", "pinTitle":"<string>","pinLink":"<string>", "pinNewFormat":"<boolean>"},
                            "youtubeData": {"title": "<string>", "type": "<string>" (default = video), "privacy": "<string>" (default = public), "tags": [ "<string>", "<string>" ], "category": "<string>" (optional field), "madeForKids": "<boolean>"},
                                Youtube type can be "video" or "short" and privacy can be "public", "unlisted" or "private".
                                Youtube category can be FILM_ANIMATION, AUTOS_VEHICLES, MUSIC, PETS_ANIMALS, SPORTS, TRAVEL_EVENTS, GAMING, PEOPLE_BLOGS, COMEDY, ENTERTAINMENT, NEWS_POLITICS, HOWTO_STYLE, EDUCATION, SCIENCE_TECHNOLOGY, NONPROFITS_ACTIVISM.
                            "twitchData": {"autoPublish":"<boolean>", "tags":[]},
                            "tiktokData": {"disableComment": "<boolean>" (default = false), "disableDuet": "<boolean>" (default = false), "disableStitch": "<boolean>" (default = false), "privacyOption": "<string>" (default = "PUBLIC_TO_EVERYONE"), "commercialContentThirdParty": "<boolean>" (default = false), "commercialContentOwnBrand": "<boolean>" (default = false), "title": "<string>", "autoAddMusic": "<boolean>" (default = false), "photoCoverIndex": "<integer>" (default = 0)},
                                Tiktok privacyOption can be "PUBLIC_TO_EVERYONE", "MUTUAL_FOLLOW_FRIENDS", "FOLLOWER_OF_CREATOR" or "SELF_ONLY".
                            "blueskyData": {"postLanguages":["",""]},
                            "threadsData":{"allowedCountryCodes:["",""]}
    """

    url = f"{METRICOOL_BASE_URL}/v2/scheduler/posts/{id}?blogId={blog_id}&userId={METRICOOL_USER_ID}&integrationSource=MCP"

    response = await make_put_request(url, data=json.dumps(info))

    if not response:
        return ("Failed to update the post")

    return response