from feed import save_images_from_rss, keywords_from_rss
from image import resize_images
from stack import stack_images
from tweet import tweet_image

# Run a cron job every hour to update image and keywords
save_images_from_rss()
resize_images()
stack_images()
keywords_from_rss()
tweet_image()
