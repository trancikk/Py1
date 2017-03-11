import pickle
import copy_reg
import types
import multiprocessing
import excel
def _pickle_method(m):
    if m.im_self is None:
        return getattr, (m.im_class, m.im_func.func_name)
    else:
        return getattr, (m.im_self, m.im_func.func_name)
    
def serialise(ob,name):
    file=name+'.data'
    output = open(file, 'wb')
    pickle.dump(ob, output, 2)
    output.close()
def load(name):
    file=name+'.data'
    input = open(file, 'rb')
    obj = pickle.load(input)
    input.close()
    return obj
copy_reg.pickle(types.MethodType, _pickle_method)