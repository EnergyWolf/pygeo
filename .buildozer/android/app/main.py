# simple GUI for pygeoip
__version__ = '1.0'

from kivy.app import App
from kivy.config import Config
#Config.set('graphics', 'height', 640)
Config.set('graphics', 'width', 320)
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty

from pygeoip import GeoIP
from socket import gethostbyaddr, gethostbyname
from re import compile, search


class RootWidget(BoxLayout):

    # these link back to the kv file
    user_input = ObjectProperty(None)
    target_str = ObjectProperty(None)
    out_key = ObjectProperty(None)
    out_val = ObjectProperty(None)

    # regex's match ip address or domain name respectively
    ip = compile(r'(?:\d+\.?){4}')
    addr = compile(r'([a-z]+://)?(www\.)?[^ ]+\.[a-z.]*')


    def __init__(self, **kwargs):
        '''
        Initialises the GeoLiteCity database
        '''
        super(RootWidget, self).__init__(**kwargs)
        self.gip = GeoIP('GeoLiteCity.dat')


    def get_info(self):
        '''
        main program logic
        '''
        # get user input
        address = self.user_input.text.lower().strip()
        host_name = ''

        # test for matches
        is_ip = search(self.ip, address)
        is_addr = search(self.addr, address)

        # deal with what we matched
        if is_ip:
            try:
                target = is_ip.string
                ip_info = self.gip.record_by_addr(target)
                # if is_ip, try to resolve host name
                try:
                    host_name = gethostbyaddr(target)[0]
                    print host_name
                except:
                    pass
            except Exception:
                self.target_str.text = "[color=#FF6600][b]Can't Connect..[/b][/color]"
                self.clear_labels()
                return
        elif is_addr:
            try:
                target = is_addr.string
                ip_info = self.gip.record_by_name(target)
                # if is_addr, try to resolve IP
                try:
                    host_name = gethostbyname(target)
                except:
                    pass
            except Exception, e:
                self.target_str.text = "[color=#FF6600][b]Can't Connect..[/b][/color]"
                self.clear_labels()
                return
        else:
            self.target_str.text = "[color=#FF6600][b]Invalid Input[/b][/color]"
            return

        if not host_name:
            host_name = target
        self.target_str.text = "[color=#B2B2B2][b]%s[/b][/color]\n\n" % host_name
        k_str, v_str = "", ""
        for k, v in ip_info.items():
            k_str += "[color=#6699FF]%s[/color]:\n" % k
            v_str += "[color=#FFFFFF]%s[/color]\n" % v

        self.out_key.text = k_str
        self.out_val.text = v_str


    def clear_labels(self):
        self.out_key.text = ''
        self.out_val.text = ''


class PyGeoApp(App):

    def build(self):
        return RootWidget()


if __name__ == "__main__":
    PyGeoApp().run()
