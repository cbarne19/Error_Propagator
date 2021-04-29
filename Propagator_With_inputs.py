#Error_propagator_no_dislay 
from numpy import pi,sin,cos,tan,e,exp
import tkinter as tk
import numpy as np 
root=tk.Tk()

root.geometry("600x400")

root.title("Error Propagator")

name_var=tk.StringVar()
Formula_var=tk.StringVar()
save_as_var=tk.StringVar()
var=tk.StringVar()
Value_var =tk.StringVar()
name_var_fin_t = tk.StringVar()


vari = []
var = []
var2 = []
ky = []    
a = []  
function = [] 
vers = [] 

def dydxs():
    exec(ky[len(ky)-1])
    exec(function[len(function)-1])
    _sub = 1e-11
    _verss = var2[len(var2)-1] 
    _versss = [] 
    _dxs = [] 
    _ds = [] 
    for i in range(len(_verss)):
        if _verss[i] != ',':
            _versss.append(_verss[i]+'='+_verss[i]+'[0]')
            _ds.append(_verss[i])
        else:
            continue            
    _dzzz = _versss
    for i in range(len(_dzzz)):
        if i+1 == len(_dzzz):        
            funcs1 = 'F('+_dzzz[i]+'+'+str(_sub*eval(_ds[i]+'[0]'))+','+str(','.join(_dzzz[i+1:len(_dzzz)]))+str(','.join(_dzzz[0:i]))+')' 
        else:
            funcs1 = 'F('+_dzzz[i]+'+'+str(_sub*eval(_ds[i]+'[0]'))+','+str(','.join(_dzzz[i+1:len(_dzzz)]))+','+str(','.join(_dzzz[0:i]))+')'
        #Second_value
        if i+1 == len(_dzzz):        
            funcs2 = 'F('+_dzzz[i]+','+str(','.join(_dzzz[i+1:len(_dzzz)]))+str(','.join(_dzzz[0:i]))+')' 
        else:
            funcs2 = 'F('+_dzzz[i]+','+str(','.join(_dzzz[i+1:len(_dzzz)]))+','+str(','.join(_dzzz[0:i]))+')'   
            
        funcs3 = '('+_ds[i]+'[0]'+'+'+str(_sub*eval(_ds[i]+'[0]'))+')'
        funcs4 = '('+_ds[i]+'[0]'+')' 

        funcss1 = eval(funcs1)
        funcss2 = eval(funcs2)
        funcss3 = eval(funcs3)
        funcss4 = eval(funcs4)
        
        _dxs.append(((funcss1)-(funcss2))/((funcss3)-(funcss4)))    
    _sqrd = np.array(_dxs)**2
    _errs = [] 
    for j in range(len(_sqrd)):
        _errs.append(eval(_ds[j]+'[1]'))
    _errsnu = np.array(_errs) 
    _errsnusq = _errsnu**2 
    _unroot = _errsnusq*_sqrd 
    _err = np.sqrt(sum(_unroot))
    return _err

varis = [] 
varis2 = [] 
def submit():   
    var.append(name_entry_Formula.get())
    var2.append(name_entry.get())
    expression = Value_entry.get()
    ky.append(var2[len(var2)-1]+'='+expression)
    form = var[len(var)-1]
    for i in range(len(expression)):
        if expression[i] != ',' and expression[i+1] != ',':
            break     
    vers.append(expression[0:i-1])
    function.append('def F('+var2[len(var2)-1]+'): \n    return '+form)
    
    exec(var2[len(var2)-1]+'='+expression)
    for i in range(len(var2[len(var2)-1])):
        if var2[len(var2)-1][i] == ',':
            continue 
        else:
            varis.append(eval(var2[len(var2)-1][i][0]))
            varis2.append(var2[len(var2)-1][i][0])
    for j in range(len(varis)):
        exec(varis2[j]+'='+str(varis[j][0]))    
    QWERTY = eval(form)
    _C = dydxs()
    name_var_fin_t.set(str(round(QWERTY,7))+'±'+str(_C))
    #print(str(round(QWERTY,7))+'±'+str(_C))
    
    
    
name_label_Formula = tk.Label(root, text = 'Input formula', font=('calibre',10, 'bold'))
name_entry_Formula = tk.Entry(root,textvariable = Formula_var,width = 40, font=('calibre',10,'normal'))

name_label = tk.Label(root, text = 'Variables', font=('calibre',10, 'bold'))
name_entry = tk.Entry(root,textvariable = name_var,width = 40, font=('calibre',10,'normal'))

Value_label = tk.Label(root, text = 'Values', font = ('calibre',10,'bold'))
Value_entry=tk.Entry(root, textvariable = Value_var, width = 40,font = ('calibre',10,'normal'))


Title = tk.Label(root, text = 'Error Propagator', font = ('calibre',15,'bold'))

sub_btn=tk.Button(root,text = 'Submit', command = submit) 

Title.grid(row=0,column = 1)
name_label_Formula.grid(row=2,column=0)
name_entry_Formula.grid(row=2,column=1)
name_label.grid(row=3,column=0)
name_entry.grid(row=3,column=1)
Value_label.grid(row=4,column=0)
Value_entry.grid(row=4,column=1)
sub_btn.grid(row=7,column=1)

name_label_fin_t = tk.Label(root, text = 'Output', font=('calibre',10, 'bold'))
name_entry_fin_t = tk.Entry(root,textvariable = name_var_fin_t, width = 40,font=('calibre',10,'normal'))


name_label_fin_t.grid(row=5,column=0)
name_entry_fin_t.grid(row=5,column=1)

Formula_var.set('a/b')
name_var.set('a,b')
Value_var.set('[10,0.25],[14,3.2]')

root.mainloop()
