import datetime
from kivy.lang import Builder
from plyer import gps,sms
from kivy.app import App
from kivy.properties import StringProperty
from kivy.clock import mainthread
from kivy.utils import platform

kv = '''
BoxLayout:
    orientation: 'vertical'

    Label:
        text: app.gps_location
    
    Label:
        text: app.gps_status
            
    TextInput:
        id: recipient
        hint_text:'Enter Cellphone Number'
        multiline: False
        on_text:app.number()
        
    BoxLayout:
        size_hint_y: None
        height: '48dp'
        padding: '4dp'

        ToggleButton:
            text: 'Start' if self.state == 'normal' else 'Stop'
            on_state:
                app.start(1000, 0) if self.state == 'down' else \
                app.stop()
                
        Button:
            text: 'SMS'
            size_hint_y: None
            height: sp(40)
            on_release: app.SMS()
        
'''


class GpsTest(App):

    gps_location = StringProperty()
    gps_status = StringProperty()
    gps_timestamp = StringProperty()

    def request_android_permissions(self):

        from android.permissions import request_permissions, Permission

        def callback(permissions, results):
            if all([res for res in results]):
                print("All permissions granted.")
            else:
                print("Some permissions refused.")

        request_permissions([Permission.ACCESS_COARSE_LOCATION,Permission.SEND_SMS,Permission.ACCESS_FINE_LOCATION], callback)

    def build(self):
        try:
            gps.configure(on_location=self.on_location,
                          on_status=self.on_status)
        except NotImplementedError:
            import traceback
            traceback.print_exc()
            self.gps_status = 'GPS is not implemented for your platform'

        if platform == "android":
            print("gps.py: Android detected. Requesting permissions")
            self.request_android_permissions()
        return Builder.load_string(kv)

    def start(self, minTime, minDistance):
        gps.start(minTime, minDistance)

    def stop(self):
        gps.stop()

    def number(self):
        self.sms_recipient=self.root.ids.recipient.text

    def SMS(self):
        sms.send(recipient=self.sms_recipient,message=self.gps_location)

    @mainthread
    def on_location(self, **kwargs):
        self.gps_location = ('\n'.join(['{}={}'.format(k, v) for k, v in kwargs.items()]) ) + '\n' + 'Time Stamp: '+str(datetime.datetime.now())

    @mainthread
    def on_status(self, stype, status):
        self.gps_status = 'type={}\n{}'.format(stype, status)

    def on_pause(self):
        return True

    def on_resume(self):
        pass


if __name__ == '__main__':
    GpsTest().run()
