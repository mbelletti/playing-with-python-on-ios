import logging
import bootstrap

from rubicon.objc import objc_method, ObjCClass
logging.debug("yippie, loaded objc")

try:
    import ctypes
    import ctypes.util
    extension = ctypes.cdll.LoadLibrary(ctypes.util.find_library("extension"))
    NSLog = extension.NSLog
    NSLog.restype = None
    NSLog.argtypes = (...)

    # autorelease block
    # [NSString stringWithUTF8String:name]; <-- s.encode("utf-8")
    # NSLog(that)
    NSLog("test")
except:
    logging.exception("Setting up real logging")

class PythonAppDelegate(ObjCClass('UIResponder')):
    def __init__(self):
        logging.debug("instance created")

    @objc_method
    def applicationDidBecomeActive(self) -> None:
        logging.debug("became active")

    @objc_method
    def application_didFinishLaunchingWithOptions_(self, application, oldStatusBarOrientation: int) -> None:
        logging.debug("finished launching %s %s", application, oldStatusBarOrientation)
        try:
            root = ObjCClass("UIViewController").alloc().init()
            nav = ObjCClass("UINavigationController").alloc().initWithRootViewController(root)
        except:
            logging.exception("terrible")


    @objc_method
    def application_didChangeStatusBarOrientation_(self, application, oldStatusBarOrientation: int) -> None:
        logging.debug("or ch %s %s", application, oldStatusBarOrientation)

logging.debug("yippie, %s defined", PythonAppDelegate)


""" Code example from Ruby:

class AppDelegate
    def application(application, didFinishLaunchingWithOptions:launchOptions)
        rootViewController = UIViewController.alloc.init
        rootViewController.title = 'Hello'
        rootViewController.view.backgroundColor = UIColor.whiteColor

        navigationController = UINavigationController.alloc.initWithRootViewController(rootViewController)

        @window = UIWindow.alloc.initWithFrame(UIScreen.mainScreen.bounds)
        @window.rootViewController = navigationController
        @window.makeKeyAndVisible

        alert = UIAlertView.new
        alert.message = "Hello iOS!"
        alert.show

        true
    end
end
"""
