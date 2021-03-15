class Translation(object):

    START_TEXT = """Hello,

I Am TamannaahAIRobot(@tamannahairobot), a Telegram URL Uploader Bot!

<b>Please send me any Direct download URL link, I can upload to Telegram as File/Video</b>

/help for more details..

Creator : @imdakshvarshney
"""

    HELP_USER = """Hi I'm a URL Uploader bot..
    
1. Send url (Link | New Name with Extension).
2. Send Custom Thumbnail (Optional).
3. Select the button.
   SVideo - Give File as video with Screenshots
   DFile  - Give File with Screenshots
   Video  - Give File as video without Screenshots
   DFile  - Give File without Screenshots

Creator : @imdakshvarshney
"""

    FORMAT_SELECTION = """Select the desired format: <a href='{}'>file size might be approximate</a>
    
Send your custum thumbnail if required.
You can use /deletethumbnail to delete the auto-generated thumbnail."""
    
    SET_CUSTOM_USERNAME_PASSWORD = """If you want to download premium videos, provide in the following format:
URL | newfilename | username | password"""


    UPGRADE_TEXT = "<b>👉 Create own Clone Bot.. </b>  \n\n<a href='https://github.com/prgofficial/URLuploader-With-Hotstar'>Click here, Fork and deploy!!</a>"
    
    DOWNLOAD_START = "Downloading Your File..."
    
    UPLOAD_START = "Now, Uploading Your File..."
    
    AFTER_SUCCESSFUL_UPLOAD_MSG_WITH_TS = "Downloaded in {} seconds. \n\nUploaded in {} seconds."

    RCHD_TG_API_LIMIT = "Downloaded in {} seconds.\nDetected File Size: {}\nSorry. But, I cannot upload files greater than 1.95GB due to Telegram API limitations."

    SAVED_CUSTOM_THUMB_NAIL = "Custom Thumbnail Saved. This will be permanent.\n\nUse /deletethumbnail to clear it."

    DEL_ETED_CUSTOM_THUMB_NAIL = "Custom Thumbnail Deleted Succesfully."

    CUSTOM_CAPTION_UL_FILE = " "

    SLOW_URL_DECED = "Gosh that seems to be a very slow URL. Since you were screwing my home, I am in no mood to download this file. Meanwhile, why don't you try this:==> https://shrtz.me/PtsVnf6 and get me a fast URL so that I can upload to Telegram, without me slowing down for other users."

    NO_VOID_FORMAT_FOUND = "ERROR...\n<b>YouTubeDL</b> said: {}"
    
    SHOW_THUMB = "Use /deletethumbnail to clear this thumbnail."
    
    NO_THUMB = "No saved thumbnails Found!!\n\nSend an image to save it as your thumbnail permanently."    
