import time
import pywemo
from tweepy import OAuthHandler, Stream, StreamListener

consumer_key=""
consumer_secret=""
access_token=""
access_token_secret=""
address=""
port = pywemo.ouimeaux_device.probe_wemo(address)
url='http://%s:%i/setup.xml' % (address, port)
device= pywemo.discovery.device_from_description(url, None)


class StdOutListener(StreamListener):
    """ A listener handles tweets that are received from the stream.
    This is a basic listener that just prints received tweets to stdout.
    """
    def on_data(self, data):
        print(data)
        if device.get_state() == 0:
            device.toggle()
        time.sleep(10)
        device.toggle()
        return True

    def on_error(self, status):
        print(status)

if __name__ == '__main__':
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    stream = Stream(auth, l)
    stream.filter(track=['animefunfact'])
