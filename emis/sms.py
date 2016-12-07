import urllib
import urllib2


class Error(Exception):
    pass

class GatewayNotAvailableError(Error):
    pass

class SmsGupshupError(Error):
    '''An sms error with two attributes - errorcode, errormessage'''
    def __init__(self, errorcode, errormessage):
        self.errorcode = errorcode
        self.errormessage = errormessage

    def __unicode__(self):
        return '[%s] %s' % (self.errorcode, self.errormessage)


class SmsGupshupFailure(SmsGupshupError):
    '''same as SmsGupshupError, but it's a temporary failure'''
    pass


class SmsGupshupSender(object):
    version = '1.0'
    url='http://enterprise.smsgupshup.com/GatewayAPI/rest'

    def __init__(self,
                 username=None,
                 password=None,
                 debug=False):
        self.username = username
        self.password = password
        self.debug = debug

    def send(self, number, message):
        '''
Sends message to number.

raises sms.Error(errorcode, errormessage)
>>> import sms
>>> s = sms.SmsGupshupSender(username='xxx', password='xxx')
>>> s.send('98xxx xxxxx', msg)
>>>
'''
        if self.debug:
            print '%s: %s' % (number, message)
            return

        params = {'method': 'sendMessage',
                  'send_to': number,
                  'msg': message,
                  'userid': self.username,
                  'password': self.password,}
        data = urllib.urlencode(params)
        the_url = self.url + '?' + data
        try:
            response = urllib2.urlopen(the_url)
        except :
            raise GatewayNotAvailableError()
        r = [x.strip() for x in response.read().split('|')]
        if r[0] != 'success':
            if len(r) == 3:
                raise SmsGupshupError(r[1], r[2])
            else:
                raise SmsGupshupFailure(r[2], r[3])
