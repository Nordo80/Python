"""Twitter."""
import itertools


class Tweet:
    """Tweet class."""

    def __init__(self, user: str, content: str, time: float, retweets: int):
        """
        Tweet constructor.

        :param user: Author of the tweet.
        :param content: Content of the tweet.
        :param time: Age of the tweet.
        :param retweets: Amount of retweets.
        """
        self.user = user
        self.content = content
        self.time = time
        self.retweets = retweets


def find_fastest_growing(tweets: list) -> Tweet:
    """
    Find the fastest growing tweet.

    A tweet is the faster growing tweet if its "retweets/time" is bigger than the other's.
    >Tweet1 is 32.5 hours old and has 64 retweets.
    >Tweet2 is 3.12 hours old and has 30 retweets.
    >64/32.5 is smaller than 30/3.12 -> tweet2 is the faster growing tweet.

    :param tweets: Input list of tweets.
    :return: Fastest growing tweet.
    """
    lala = 0
    for i in tweets:
        tweet = i
        popular_tweet = tweet.retweets / tweet.time
        if popular_tweet >= lala:
            lala = popular_tweet
            main_tweet = tweet
    return main_tweet


def sort_by_popularity(tweets: list) -> list:
    """
    Sort tweets by popularity.

    Tweets must be sorted in descending order.
    A tweet is more popular than the other if it has more retweets.
    If the retweets are even, the newer tweet is the more popular one.
    >Tweet1 has 10 retweets.
    >Tweet2 has 30 retweets.
    >30 is bigger than 10 -> tweet2 is the more popular one.

    :param tweets: Input list of tweets.
    :return: List of tweets by popularity
    """
    tweets.sort(key=lambda x: x.time, reverse=False)
    tweets.sort(key=lambda x: x.retweets, reverse=True)

    return tweets


def filter_by_hashtag(tweets: list, hashtag: str) -> list:
    """
    Filter tweets by hashtag.

    Return a list of all tweets that contain given hashtag.

    :param tweets: Input list of tweets.
    :param hashtag: Hashtag to filter by.
    :return: Filtered list of tweets.
    """
    hashtag_list = []
    for tweet in tweets:
        if tweet.content.find(hashtag) != -1:
            hashtag_list.append(tweet)
    return hashtag_list


def sort_hashtags_by_popularity(tweets: list) -> list:
    """
    Sort hashtags by popularity.

    Hashtags must be sorted in descending order.
    A hashtag's popularity is the sum of its tweets' retweets.
    If two hashtags are equally popular, sort by alphabet from A-Z to a-z (upper case before lower case).
    >Tweet1 has 21 retweets and has common hashtag.
    >Tweet2 has 19 retweets and has common hashtag.
    >The popularity of that hashtag is 19 + 21 = 40.

    :param tweets: Input list of tweets.
    :return: List of hashtags by popularity.
    """
    dictionary = {}
    list_list = []
    for tweet in tweets:
        splited_slova = tweet.content.split("#")
        if len(splited_slova) <= 1:
            continue
        key = "#" + splited_slova[-1]
        print(key)
        if key in dictionary.keys():
            dictionary[key] = tweet.retweets + dictionary[key]
        else:
            dictionary[key] = tweet.retweets

    sorting = sorted(dictionary.items(), key=lambda x: x[1], reverse=True)
    result = []
    for k, v in itertools.groupby(sorting, lambda x: x[1]):
        result.extend(sorted(v))
    print(result)
    for key, value in result:
        list_list.append(key)
    print(list_list)
    return list_list


if __name__ == '__main__':
    tweet1 = Tweet("@realDonaldTrump", "Despite the negative press covfefe #Abdul", 1249, 284200)
    tweet2 = Tweet("@elonmusk", "Technically, alcohol is a solution #abdul", 366.4, 284200)
    tweet3 = Tweet("@CIA", "We can neither confirm nor deny that this is our first tweet. #bigsmart", 2192, 284200)
    tweet4 = Tweet("@elonmusk", "We can neither confirm nor deny that this is our first tweet. #bigsmart", 1200, 284200)
    tweet5 = Tweet("@realDonaldTrump", "We can neither nor deny that this is our first tweet. #Boris", 2193, 284200)
    tweet6 = Tweet("@das", "We can neither nor deny that this is our first tweet. #heart", 2192, 284200)
    tweets = [tweet1, tweet2, tweet3, tweet4, tweet5, tweet6]

    print("find_fastest_growing")
    print(find_fastest_growing(tweets).user)  # -> "@elonmusk"

    print("\nsort_by_popularity")
    filtered_by_popularity = sort_by_popularity(tweets)
    print(filtered_by_popularity[0].user)  # -> "@CIA"
    print(filtered_by_popularity[1].user)  # -> "@elonmusk"
    print(filtered_by_popularity[2].user)  # -> "@realDonaldTrump"
    print(filtered_by_popularity[3].user)
    print(filtered_by_popularity[4].user)
    print(filtered_by_popularity[5].user)

    print("\nfilter_by_hashtag")
    filtered_by_hashtag = filter_by_hashtag(tweets, "#bigsmart")
    print(filtered_by_hashtag[0].user)  # -> "@realDonaldTrump"
    print(filtered_by_hashtag[1].user)  # -> "@elonMusk"

    print("\nsort_hashtags_by_popularity")
    sorted_hashtags = sort_hashtags_by_popularity(tweets)
    print(sorted_hashtags[0])  # -> "#heart"
