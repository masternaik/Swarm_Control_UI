# This file was automatically generated by SWIG (http://www.swig.org).
# Version 2.0.11
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.





from sys import version_info
if version_info >= (2,6,0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_ADC', [dirname(__file__)])
        except ImportError:
            import _ADC
            return _ADC
        if fp is not None:
            try:
                _mod = imp.load_module('_ADC', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _ADC = swig_import_helper()
    del swig_import_helper
else:
    import _ADC
del version_info
try:
    _swig_property = property
except NameError:
    pass # Python < 2.2 doesn't have 'property'.
def _swig_setattr_nondynamic(self,class_type,name,value,static=1):
    if (name == "thisown"): return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name,None)
    if method: return method(self,value)
    if (not static):
        self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)

def _swig_setattr(self,class_type,name,value):
    return _swig_setattr_nondynamic(self,class_type,name,value,0)

def _swig_getattr(self,class_type,name):
    if (name == "thisown"): return self.this.own()
    method = class_type.__swig_getmethods__.get(name,None)
    if method: return method(self)
    raise AttributeError(name)

def _swig_repr(self):
    try: strthis = "proxy of " + self.this.__repr__()
    except: strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

try:
    _object = object
    _newclass = 1
except AttributeError:
    class _object : pass
    _newclass = 0


class Joystick(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, Joystick, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, Joystick, name)
    __repr__ = _swig_repr
    __swig_setmethods__["value"] = _ADC.Joystick_value_set
    __swig_getmethods__["value"] = _ADC.Joystick_value_get
    if _newclass:value = _swig_property(_ADC.Joystick_value_get, _ADC.Joystick_value_set)
    __swig_setmethods__["min"] = _ADC.Joystick_min_set
    __swig_getmethods__["min"] = _ADC.Joystick_min_get
    if _newclass:min = _swig_property(_ADC.Joystick_min_get, _ADC.Joystick_min_set)
    __swig_setmethods__["mid"] = _ADC.Joystick_mid_set
    __swig_getmethods__["mid"] = _ADC.Joystick_mid_get
    if _newclass:mid = _swig_property(_ADC.Joystick_mid_get, _ADC.Joystick_mid_set)
    __swig_setmethods__["max"] = _ADC.Joystick_max_set
    __swig_getmethods__["max"] = _ADC.Joystick_max_get
    if _newclass:max = _swig_property(_ADC.Joystick_max_get, _ADC.Joystick_max_set)
    def __init__(self): 
        this = _ADC.new_Joystick()
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _ADC.delete_Joystick
    __del__ = lambda self : None;
Joystick_swigregister = _ADC.Joystick_swigregister
Joystick_swigregister(Joystick)


def get_adc_value(*args):
  return _ADC.get_adc_value(*args)
get_adc_value = _ADC.get_adc_value

def get_all_values(*args):
  return _ADC.get_all_values(*args)
get_all_values = _ADC.get_all_values

def initialize_joystick(*args):
  return _ADC.initialize_joystick(*args)
initialize_joystick = _ADC.initialize_joystick

def print_all_values(*args):
  return _ADC.print_all_values(*args)
print_all_values = _ADC.print_all_values
# This file is compatible with both classic and new-style classes.


