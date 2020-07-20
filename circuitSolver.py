#!/usr/bin/python3

import SchemDraw as schem
import SchemDraw.elements as e
import sympy

__authors__ = ["Alireza Zarenejad", "Moein Shafi"]
__copyright__ = "Copyright 2020"
__credits__ = ["Alireza Zarenejad", "Moein Shafi"]
__license__ = "GPL3"
__version__ = "0.0.1"
__maintainers__ = ["Alireza Zarenejad", "Moein Shafi"]
__emails__ = ["a.zarenejad@gmail.com", "mosafer.moein@gmail.com"]
__status__ = "Production"

class element:
    def __init__(self, kind, position, value = 0, dposition = "", dtype = "", a = 0, b = 0):
        self.kind = kind
        self.position = position
        self.value = value
        self.dposition = dposition
        self.dtype = dtype
        self.a = a
        self.b = b


class circuitEx(Exception):
    def __init__(self, msg=""):
        print('**')
        print('** Circuit exception')
        print('**')
        print('** ' + msg)
        print('**')
        print("\n")


class circuit():
    def __init__(self):
        self.components = []
        self.subsDic = {}
        self.meas = {}
        self.sSolution = None
        self.solution = None
        self.particular = None
        self.name = {}
        self.symbol = {}
        if verbose:
            print('Starting a new circuit')
        self.elements = []
        self.results = []


    def addR(self,name,node1,node2,value=None):
        sy = sympy.Symbol(name)

        dict = {}
        dict['k']  = 'r'
        dict['n']  = name
        dict['n1'] = node1
        dict['n2'] = node2
        dict['v']  = value
        dict['sy'] = sy

        self.components.append(dict)

        self.symbol[name] = sy

        if value != None:
            self.subsDic[sy] = value
        if verbose:
            if value:
                print('Resistor',name,'added between nodes',node1,'and',node2,'with value',value)
            else:
                print('Resistor',name,'added between nodes',node1,'and',node2)
        return sy

    def addC(self,name,node1,node2,value=None):
        sy = sympy.Symbol(name)

        dict = {}
        dict['k']  = 'c'
        dict['n']  = name
        dict['n1'] = node1
        dict['n2'] = node2
        dict['v']  = value
        dict['sy'] = sy

        self.components.append(dict)

        self.symbol[name] = sy

        if value != None:
            self.subsDic[sy] = value
        if verbose:
            if value:
                print('Capcitor',name,'added between nodes',node1,'and',node2,'with value',value)
            else:
                print('Capacitor',name,'added between nodes',node1,'and',node2)
        return sy

    def addL(self,name,node1,node2,value=None):
        sy = sympy.Symbol(name)

        dict = {}
        dict['k']  = 'l'
        dict['n']  = name
        dict['n1'] = node1
        dict['n2'] = node2
        dict['v']  = value
        dict['sy'] = sy

        self.components.append(dict)

        self.symbol[name] = sy

        if value != None:
            self.subsDic[sy] = value
        if verbose:
            if value:
                print('Inductor',name,'added between nodes',node1,'and',node2,'with value',value)
            else:
                print('Inductor',name,'added between nodes',node1,'and',node2)
        return sy

    def addV(self,name,node1,node2,value=None):
        sy = sympy.Symbol(name)

        dict = {}
        dict['k']  = 'vs'
        dict['n']  = name
        dict['n1'] = node1
        dict['n2'] = node2
        dict['v']  = value
        dict['sy'] = sy

        isy = sympy.Symbol('i'+name)
        dict['isy'] = isy

        self.name[isy] = 'i'+name

        self.symbol[name] = sy
        self.symbol['i'+name] = isy

        self.components.append(dict)

        if value != None:
            self.subsDic[sy] = value
        if verbose:
            if value:
                print('Voltage supply',name,'added between nodes',node1,'and',node2,'with value',value)
            else:
                print('Voltage supply',name,'added between nodes',node1,'and',node2)
        return sy

    def addI(self,name,node1,node2,value=None):
        sy = sympy.Symbol(name)

        dict = {}
        dict['k']  = 'is'
        dict['n']  = name
        dict['n1'] = node1
        dict['n2'] = node2
        dict['v']  = value
        dict['sy'] = sy

        self.components.append(dict)

        self.symbol[name] = sy

        if value != None:
            self.subsDic[sy] = value
        if verbose:
            if value:
                print('Current supply',name,'added between nodes',node1,'and',node2,'with value',value)
            else:
                print('Current supply',name,'added between nodes',node1,'and',node2)
        return sy

    def addVM(self,name,node1,node2):
        sy = sympy.Symbol(name)

        dict = {}
        dict['k']  = 'vm'
        dict['n']  = name
        dict['n1'] = node1
        dict['n2'] = node2
        dict['sy'] = sy

        self.name[sy] = name

        self.symbol[name] = sy

        self.components.append(dict)

        self.meas[name] = dict
        if verbose:
            print('Voltage measurement',name,'added between nodes',node1,'and',node2)
        return sy

    def addIM(self,name,node1,node2):
        sy = sympy.Symbol(name)

        dict = {}
        dict['k']  = 'im'
        dict['n']  = name
        dict['n1'] = node1
        dict['n2'] = node2
        dict['sy'] = sy

        self.name[sy] = name

        self.symbol[name] = sy

        self.components.append(dict)

        self.meas[name] = dict
        if verbose:
            print('Current measurement',name,'added between nodes',node1,'and',node2)
        return sy

    def addCVS(self,name,node1,node2,cont,value=None):
        try:
            ctr = self.meas[cont]
        except KeyError:
            raise circuitEx('CVS controller must be defined previously')

        sy = sympy.Symbol(name)

        dict = {}
        dict['k']  = 'cvs'
        dict['n']  = name
        dict['n1'] = node1
        dict['n2'] = node2
        dict['v']  = value
        dict['sy'] = sy
        dict['ctr'] = ctr

        isy = sympy.Symbol('i'+name)
        dict['isy'] = isy

        self.name[isy] = 'i'+name

        self.symbol[name] = sy
        self.symbol['i'+name] = isy

        self.components.append(dict)

        if value != None:
            self.subsDic[sy] = value
        if verbose:
            if value:
                print('VcVs',name,'added between nodes',node1,'and',node2,'with value',value)
            else:
                print('VcVs',name,'added between nodes',node1,'and',node2)
        return sy

    def addCIS(self,name,node1,node2,cont,value=None):
        try:
            ctr = self.meas[cont]
        except KeyError:
            raise circuitEx('CIS controller must be defined previously')

        sy = sympy.Symbol(name)

        dict = {}
        dict['k']  = 'cis'
        dict['n']  = name
        dict['n1'] = node1
        dict['n2'] = node2
        dict['v']  = value
        dict['sy'] = sy
        dict['ctr'] = ctr

        self.components.append(dict)

        self.symbol[name] = sy

        if value != None:
            self.subsDic[sy] = value
        if verbose:
            if value:
                print('Current supply',name,'added between nodes',node1,'and',node2,'with value',value)
            else:
                print('Current supply',name,'added between nodes',node1,'and',node2)
        return sy


    def _numNodes(self):
        self.nodeList = set([])

        if len(self.components)==0:
            raise circuitEx('No components in the circuit')

        for component in self.components:
            self.nodeList.add(component['n1'])
            self.nodeList.add(component['n2'])

        self.nodeList = list(self.nodeList)
        if verbose:
            print('There are',len(self.nodeList),'nodes :')
            for node in self.nodeList:
                print('    ',node)

    def _nodeVariables(self):
        self.nodeVars = {}

        if len(self.nodeList) == 0:
            raise circuitEx('No nodes in the circuit')
        if verbose:
            print('Creating node variables')
        zeroFound = False
        for node in self.nodeList:
            if node == 0:
                zeroFound = True
            else:
                name = 'v'+str(node)
                ns = sympy.Symbol(name)
                self.nodeVars[node] = ns
                self.unknowns.add(ns)

                self.name[ns] = name

                self.symbol[name] = ns
                if verbose:
                    print('    ',name)
        if not zeroFound:
            raise circuitEx('No 0 node in circuit')

    def _addRtoNode(self,res,eq,node):
        n1 = res['n1']
        n2 = res['n2']
        if n1 == node:
            if n2 == 0:
                eq = eq - self.nodeVars[n1]/res['sy']
            else:
                eq = eq - (self.nodeVars[n1]-self.nodeVars[n2])/res['sy']
        if n2 == node:
            if n1 == 0:
                eq = eq - self.nodeVars[n2]/res['sy']
            else:
                eq = eq - (self.nodeVars[n2]-self.nodeVars[n1])/res['sy']
        return eq

    def _addCtoNode(self,cap,eq,node):
        n1 = cap['n1']
        n2 = cap['n2']
        if n1 == node:
            if n2 == 0:
                eq = eq - cap['sy']*s*self.nodeVars[n1]
            else:
                eq = eq - cap['sy']*s*(self.nodeVars[n1]-self.nodeVars[n2])
        if n2 == node:
            if n1 == 0:
                eq = eq - cap['sy']*s*self.nodeVars[n2]
            else:
                eq = eq - cap['sy']*s*(self.nodeVars[n2]-self.nodeVars[n1])
        return eq

    def _addLtoNode(self,ind,eq,node):
        n1 = ind['n1']
        n2 = ind['n2']
        if n1 == node:
            if n2 == 0:
                eq = eq - self.nodeVars[n1]/(ind['sy']*s)
            else:
                eq = eq - (self.nodeVars[n1]-self.nodeVars[n2])/(ind['sy']*s)
        if n2 == node:
            if n1 == 0:
                eq = eq - self.nodeVars[n2]/(ind['sy']*s)
            else:
                eq = eq - (self.nodeVars[n2]-self.nodeVars[n1])/(ind['sy']*s)
        return eq

    def _addVtoNode(self,vs,eq,node):
        n1 = vs['n1']
        n2 = vs['n2']
        if n1 == node:
            eq = eq + vs['isy']
        if n2 == node:
            eq = eq - vs['isy']
        return eq

    def _addItoNode(self,isr,eq,node):
        n1 = isr['n1']
        n2 = isr['n2']
        if n1 == node:
            eq = eq + isr['sy']
        if n2 == node:
            eq = eq - isr['sy']
        return eq

    def _addIMtoNode(self,im,eq,node):
        n1 = im['n1']
        n2 = im['n2']
        if n1 == node:
            eq = eq + im['sy']
        if n2 == node:
            eq = eq - im['sy']
        return eq

    def _addKCLequations(self):
        if verbose:
            print('Creating KCL equations')
        for node in self.nodeList:
            if node != 0:
                equation = sympy.Rational(0,1)
                for cm in self.components:
                    if cm['k'] == 'r':
                        equation = self._addRtoNode(cm,equation,node)
                    elif cm['k'] == 'c':
                        equation = self._addCtoNode(cm,equation,node)
                    elif cm['k'] == 'l':
                        equation = self._addLtoNode(cm,equation,node)
                    elif cm['k'] == 'vs' or cm['k'] == 'cvs':
                        equation = self._addVtoNode(cm,equation,node)
                    elif cm['k'] == 'is' or cm['k'] == 'cis':
                        equation = self._addItoNode(cm,equation,node)
                    elif cm['k'] == 'im':
                        equation = self._addIMtoNode(cm,equation,node)
                self.equations.append(equation)
                if verbose:
                    print('    ',equation)

    def _substEqs(self,oldS,newS):
        newList = []
        for eq in self.equations:
            newList.append(eq.subs(oldS,newS))
        self.equations = newList

    def _addVequations(self):
        if verbose:
            print('Adding V source equations')
        for cm in self.components:
            if cm['k']=='vs' or cm['k']=='cvs':

                self.unknowns.add(cm['isy'])
                n1 = cm['n1']
                n2 = cm['n2']
                if   n1 == 0:
                    self.equations.append(sympy.Eq(cm['sy'],-self.nodeVars[n2]))
                elif n2 == 0:
                    self.equations.append(sympy.Eq(cm['sy'],self.nodeVars[n1]))
                else:
                    self.equations.append(sympy.Eq(cm['sy'],self.nodeVars[n1]-self.nodeVars[n2]))

    def _processVM(self):
        if verbose:
            print('Adding V measurement equations')
        for cm in self.components:
            if cm['k']=='vm':

                self.unknowns.add(cm['sy'])
                n1 = cm['n1']
                n2 = cm['n2']
                if   n1 == 0:
                    self._substEqs(self.nodeVars[n2],-cm['sy'])
                    try:
                        self.unknowns.remove(self.nodeVars[n2])
                    except KeyError:
                        self.equations.append(sympy.Eq(cm['sy'],self.nodeVars[n2]))
                elif n2 == 0:
                    self._substEqs(self.nodeVars[n1],cm['sy'])
                    try:
                        self.unknowns.remove(self.nodeVars[n1])
                    except KeyError:
                        self.equations.append(sympy.Eq(cm['sy'],self.nodeVars[n1]))
                else:
                    self.equations.append(sympy.Eq(cm['sy'],self.nodeVars[n1]-self.nodeVars[n2]))

    def _processIM(self):
        if verbose:
            print('Adding I measurement equations')
        for cm in self.components:
            if cm['k']=='im':
                self.unknowns.add(cm['sy'])
                n1 = cm['n1']
                n2 = cm['n2']
                if n1 == 0:
                    self._substEqs(self.nodeVars[n2],0)
                    self.unknowns.remove(self.nodeVars[n2])
                    self.nodeVars[n2] = 0
                elif n2 == 0:
                    self._substEqs(self.nodeVars[n1],0)
                    self.unknowns.remove(self.nodeVars[n1])
                    self.nodeVars[n1] = 0
                else:
                    self._substEqs(self.nodeVars[n1],self.nodeVars[n2])
                    self.unknowns.remove(self.nodeVars[n1])
                    self.nodeVars[n1] = self.nodeVars[n2]

    def _processCtr(self):
        if verbose:
            print('Processing controlled elements')
        for cm in self.components:
            if cm['k'] == 'cvs' or cm['k'] == 'cis':
                self._substEqs(cm['sy'],cm['sy']*cm['ctr']['sy'])

    def _showEquations(self):
        print('Circuit equations:')
        for eq in self.equations:
            print('    ',eq)

    def _solveEquations(self):
        if verbose:
            print('Unknowns:',self.unknowns)
        self.sSolution = sympy.solve(self.equations,list(self.unknowns))

    def _nameSolution(self):
        self.solution = {}
        for sym in self.sSolution:
            key = self.name[sym]
            self.solution[key] = self.sSolution[sym]
        if verbose:
            print('Circuit solution:')
            print('    ',self.solution)

    def _substituteSolution(self):
        self.particular = {}
        for key in self.solution:
            self.particular[key] = self.solution[key].subs(self.subsDic)
        if verbose:
            print('Circuit solution with substitutions:')
            print('    ',self.particular)

    def solve(self):
        if verbose:
            print('Solving the circuit')

        self.equations  = []
        self.unknowns = set([])
        self._numNodes()
        self._nodeVariables()
        self._addKCLequations()
        self._addVequations()
        self._processIM()
        self._processVM()
        self._processCtr()
        if verbose:
            self._showEquations()
        self._solveEquations()
        self._nameSolution()
        self._substituteSolution()
        return self.particular

    def subs(self):
        return self.particular


    def drawCircuit(self):
        d = schem.Drawing(unit=2, fontsize=12, font='monospace')
        d1 = d.add(e.DOT)
        l12 = d.add(e.LINE, d='down', xy = d1.end, color='white')
        d2 = d.add(e.DOT, xy = l12.end)
        l23 = d.add(e.LINE, d='down', xy = d2.end, color='white')
        d3 = d.add(e.DOT, xy = l23.end)
        l14 = d.add(e.LINE, d='right', xy = d1.end, color='white')
        d4 = d.add(e.DOT, xy = l14.end)
        l45 = d.add(e.LINE, d='down', xy = d4.end, color='white')
        d5 = d.add(e.DOT, xy = l45.end)
        l56 = d.add(e.LINE, d='down', xy = d5.end, color='white')
        d6 = d.add(e.DOT, xy = l56.end)
        l47 = d.add(e.LINE, d='right', xy = d4.end, color='white')
        d7 = d.add(e.DOT, xy = l47.end)
        l78 = d.add(e.LINE, d='down', xy = d7.end, color='white')
        d8 = d.add(e.DOT, xy = l78.end)
        l89 = d.add(e.LINE, d='down', xy = d8.end, color='white')
        d9 = d.add(e.DOT, xy = l89.end)
        l25 = d.add(e.LINE, d='right', xy = d2.end, color='white')
        l58 = d.add(e.LINE, d='right', xy = d5.end, color='white')
        l36 = d.add(e.LINE, d='right', xy = d3.end, color='white')
        l69 = d.add(e.LINE, d='right', xy = d6.end, color='white')
        gnd = d.add(e.GND, d='right', xy = l56.end, color='black')

        for elem in self.elements:
            if elem.position == '12':
                if (elem.kind == 'Resistor'):
                    R1 = d.add(e.RES, d='down', label=str(elem.value)+'$\Omega$', xy = l12.start)
                elif (elem.kind == 'Capacitor'):
                    R1 = d.add(e.CAP, d='down', label=str(elem.value)+'F', xy = l12.start)
                elif (elem.kind == 'Inductor'):
                    R1 = d.add(e.INDUCTOR, d='down', label=str(elem.value)+'H', xy = l12.start)
                elif (elem.kind == 'Voltage Independent Source'):
                    S1 = d.add(e.SOURCE_V, d='down', label=str(elem.value)+'V', xy = l12.start)
                elif (elem.kind == 'Current Independent Source'):
                    S1 = d.add(e.SOURCE_I, d='down', label=str(elem.value)+'A', xy = l12.start)
                elif (elem.kind == 'Voltage Dependent Source'):
                    S1 = d.add(e.SOURCE_CONT_V, d='down', label=str(elem.a)+elem.dtype+elem.dposition+' + '+str(elem.b), xy = l12.start)
                elif (elem.kind == 'Current Dependent Source'):
                    S1 = d.add(e.SOURCE_CONT_I, d='down', label=str(elem.a)+elem.dtype+elem.dposition+' + '+str(elem.b), xy = l12.start)
                l12.color = 'none'
                if (elem.kind == 'Wire'):
                    # l12.color = 'black'
                    l12 = d.add(e.LINE, d='down', xy = d1.end, color='black')
            if elem.position == '21':
                if (elem.kind == 'Resistor'):
                    R1 = d.add(e.RES, d='up', label=str(elem.value)+'$\Omega$', xy = l12.end)
                elif (elem.kind == 'Capacitor'):
                    R1 = d.add(e.CAP, d='up', label=str(elem.value)+'F', xy = l12.end)
                elif (elem.kind == 'Inductor'):
                    R1 = d.add(e.INDUCTOR, d='up', label=str(elem.value)+'H', xy = l12.end)
                elif (elem.kind == 'Voltage Independent Source'):
                    S1 = d.add(e.SOURCE_V, d='up', label=str(elem.value)+'V', xy = l12.end)
                elif (elem.kind == 'Current Independent Source'):
                    S1 = d.add(e.SOURCE_I, d='up', label=str(elem.value)+'A', xy = l12.end)
                elif (elem.kind == 'Voltage Dependent Source'):
                    S1 = d.add(e.SOURCE_CONT_V, d='up', label=str(elem.a)+elem.dtype+elem.dposition+' + '+str(elem.b), xy = l12.end)
                elif (elem.kind == 'Current Dependent Source'):
                    S1 = d.add(e.SOURCE_CONT_I, d='up', label=str(elem.a)+elem.dtype+elem.dposition+' + '+str(elem.b), xy = l12.end)
                l12.color = 'none'
                if (elem.kind == 'Wire'):
                    # l12.color = 'black'
                    l12 = d.add(e.LINE, d='down', xy = d1.end, color='black')
            elif elem.position == '23':
                if (elem.kind == 'Resistor'):
                    R2 = d.add(e.RES, d='down', label=str(elem.value)+'$\Omega$', xy = l23.start)
                elif (elem.kind == 'Capacitor'):
                    R1 = d.add(e.CAP, d='down', label=str(elem.value)+'F', xy = l23.start)
                elif (elem.kind == 'Inductor'):
                    R1 = d.add(e.INDUCTOR, d='down', label=str(elem.value)+'H', xy = l23.start)
                elif (elem.kind == 'Voltage Independent Source'):
                    S2 = d.add(e.SOURCE_V, d='down', label=str(elem.value)+'V', xy = l23.start)
                elif (elem.kind == 'Current Independent Source'):
                    S2 = d.add(e.SOURCE_I, d='down', label=str(elem.value)+'A', xy = l23.start)
                elif (elem.kind == 'Voltage Dependent Source'):
                    S2 = d.add(e.SOURCE_CONT_V, d='down', label=str(elem.a)+elem.dtype+elem.dposition+' + '+str(elem.b), xy = l23.start)
                elif (elem.kind == 'Current Dependent Source'):
                    S2 = d.add(e.SOURCE_CONT_I, d='down', label=str(elem.a)+elem.dtype+elem.dposition+' + '+str(elem.b), xy = l23.start)
                l23.color = 'none'
                if (elem.kind == 'Wire'):
                    # l23.color = 'black'
                    l23 = d.add(e.LINE, d='down', xy = d2.end, color='black')
            elif elem.position == '32':
                if (elem.kind == 'Resistor'):
                    R2 = d.add(e.RES, d='up', label=str(elem.value)+'$\Omega$', xy = l23.end)
                elif (elem.kind == 'Capacitor'):
                    R1 = d.add(e.CAP, d='up', label=str(elem.value)+'F', xy = l23.end)
                elif (elem.kind == 'Inductor'):
                    R1 = d.add(e.INDUCTOR, d='up', label=str(elem.value)+'H', xy = l23.end)
                elif (elem.kind == 'Voltage Independent Source'):
                    S2 = d.add(e.SOURCE_V, d='up', label=str(elem.value)+'V', xy = l23.end)
                elif (elem.kind == 'Current Independent Source'):
                    S2 = d.add(e.SOURCE_I, d='up', label=str(elem.value)+'A', xy = l23.end)
                elif (elem.kind == 'Voltage Dependent Source'):
                    S2 = d.add(e.SOURCE_CONT_V, d='up', label=str(elem.a)+elem.dtype+elem.dposition+' + '+str(elem.b), xy = l23.end)
                elif (elem.kind == 'Current Dependent Source'):
                    S2 = d.add(e.SOURCE_CONT_I, d='up', label=str(elem.a)+elem.dtype+elem.dposition+' + '+str(elem.b), xy = l23.end)
                l23.color = 'none'
                if (elem.kind == 'Wire'):
                    # l23.color = 'black'
                    l23 = d.add(e.LINE, d='down', xy = d2.end, color='black')
            elif elem.position == '58':
                if (elem.kind == 'Resistor'):
                    R3 = d.add(e.RES, d='right', label=str(elem.value)+'$\Omega$', xy = l58.start)
                elif (elem.kind == 'Capacitor'):
                    R1 = d.add(e.CAP, d='right', label=str(elem.value)+'F', xy = l58.start)
                elif (elem.kind == 'Inductor'):
                    R1 = d.add(e.INDUCTOR, d='right', label=str(elem.value)+'H', xy = l58.start)
                elif (elem.kind == 'Voltage Independent Source'):
                    S3 = d.add(e.SOURCE_V, d='right', label=str(elem.value)+'V', xy = l58.start)
                elif (elem.kind == 'Current Independent Source'):
                    S3 = d.add(e.SOURCE_I, d='right', label=str(elem.value)+'A', xy = l58.start)
                elif (elem.kind == 'Voltage Dependent Source'):
                    S3 = d.add(e.SOURCE_CONT_V, d='right', label=str(elem.a)+elem.dtype+elem.dposition+' + '+str(elem.b), xy = l58.start)
                elif (elem.kind == 'Current Dependent Source'):
                    S3 = d.add(e.SOURCE_CONT_I, d='right', label=str(elem.a)+elem.dtype+elem.dposition+' + '+str(elem.b), xy = l58.start)
                l58.color = 'none'
                if (elem.kind == 'Wire'):
                    # l58.color = 'black'
                    l58 = d.add(e.LINE, d='right', xy = d5.end, color='black')
            elif elem.position == '85':
                if (elem.kind == 'Resistor'):
                    R3 = d.add(e.RES, d='left', label=str(elem.value)+'$\Omega$', xy = l58.end)
                elif (elem.kind == 'Capacitor'):
                    R1 = d.add(e.CAP, d='left', label=str(elem.value)+'F', xy = l58.end)
                elif (elem.kind == 'Inductor'):
                    R1 = d.add(e.INDUCTOR, d='left', label=str(elem.value)+'H', xy = l58.end)
                elif (elem.kind == 'Voltage Independent Source'):
                    S3 = d.add(e.SOURCE_V, d='left', label=str(elem.value)+'V', xy = l58.end)
                elif (elem.kind == 'Current Independent Source'):
                    S3 = d.add(e.SOURCE_I, d='left', label=str(elem.value)+'A', xy = l58.end)
                elif (elem.kind == 'Voltage Dependent Source'):
                    S3 = d.add(e.SOURCE_CONT_V, d='left', label=str(elem.a)+elem.dtype+elem.dposition+' + '+str(elem.b), xy = l58.end)
                elif (elem.kind == 'Current Dependent Source'):
                    S3 = d.add(e.SOURCE_CONT_I, d='left', label=str(elem.a)+elem.dtype+elem.dposition+' + '+str(elem.b), xy = l58.end)
                l58.color = 'none'
                if (elem.kind == 'Wire'):
                    # l58.color = 'black'
                    l58 = d.add(e.LINE, d='right', xy = d5.end, color='black')
            elif elem.position == '14':
                if (elem.kind == 'Resistor'):
                    R4 = d.add(e.RES, d='right', label=str(elem.value)+'$\Omega$', xy = l14.start)
                elif (elem.kind == 'Capacitor'):
                    R1 = d.add(e.CAP, d='right', label=str(elem.value)+'F', xy = l14.start)
                elif (elem.kind == 'Inductor'):
                    R1 = d.add(e.INDUCTOR, d='right', label=str(elem.value)+'H', xy = l14.start)
                elif (elem.kind == 'Voltage Independent Source'):
                    S4 = d.add(e.SOURCE_V, d='right', label=str(elem.value)+'V', xy = l14.start)
                elif (elem.kind == 'Current Independent Source'):
                    S4 = d.add(e.SOURCE_I, d='right', label=str(elem.value)+'A', xy = l14.start)
                elif (elem.kind == 'Voltage Dependent Source'):
                    S4 = d.add(e.SOURCE_CONT_V, d='right', label=str(elem.a)+elem.dtype+elem.dposition+' + '+str(elem.b), xy = l14.start)
                elif (elem.kind == 'Current Dependent Source'):
                    S4 = d.add(e.SOURCE_CONT_I, d='right', label=str(elem.a)+elem.dtype+elem.dposition+' + '+str(elem.b), xy = l14.start)
                l14.color = 'none'
                if (elem.kind == 'Wire'):
                    # l14.color = 'black'
                    l14 = d.add(e.LINE, d='right', xy = d1.end, color='black')
            elif elem.position == '41':
                if (elem.kind == 'Resistor'):
                    R4 = d.add(e.RES, d='left', label=str(elem.value)+'$\Omega$', xy = l14.end)
                elif (elem.kind == 'Capacitor'):
                    R1 = d.add(e.CAP, d='left', label=str(elem.value)+'F', xy = l14.end)
                elif (elem.kind == 'Inductor'):
                    R1 = d.add(e.INDUCTOR, d='left', label=str(elem.value)+'H', xy = l14.end)
                elif (elem.kind == 'Voltage Independent Source'):
                    S4 = d.add(e.SOURCE_V, d='left', label=str(elem.value)+'V', xy = l14.end)
                elif (elem.kind == 'Current Independent Source'):
                    S4 = d.add(e.SOURCE_I, d='left', label=str(elem.value)+'A', xy = l14.end)
                elif (elem.kind == 'Voltage Dependent Source'):
                    S4 = d.add(e.SOURCE_CONT_V, d='left', label=str(elem.a)+elem.dtype+elem.dposition+' + '+str(elem.b), xy = l14.end)
                elif (elem.kind == 'Current Dependent Source'):
                    S4 = d.add(e.SOURCE_CONT_I, d='left', label=str(elem.a)+elem.dtype+elem.dposition+' + '+str(elem.b), xy = l14.end)
                l14.color = 'none'
                if (elem.kind == 'Wire'):
                    # l14.color = 'black'
                    l14 = d.add(e.LINE, d='right', xy = d1.end, color='black')
            elif elem.position == '47':
                if (elem.kind == 'Resistor'):
                    R5 = d.add(e.RES, d='right', label=str(elem.value)+'$\Omega$', xy = l47.start)
                elif (elem.kind == 'Capacitor'):
                    R1 = d.add(e.CAP, d='right', label=str(elem.value)+'F', xy = l47.start)
                elif (elem.kind == 'Inductor'):
                    R1 = d.add(e.INDUCTOR, d='right', label=str(elem.value)+'H', xy = l47.start)
                elif (elem.kind == 'Voltage Independent Source'):
                    S5 = d.add(e.SOURCE_V, d='right', label=str(elem.value)+'V', xy = l47.start)
                elif (elem.kind == 'Current Independent Source'):
                    S5 = d.add(e.SOURCE_I, d='right', label=str(elem.value)+'A', xy = l47.start)
                elif (elem.kind == 'Voltage Dependent Source'):
                    S5 = d.add(e.SOURCE_CONT_V, d='right', label=str(elem.a)+elem.dtype+elem.dposition+' + '+str(elem.b), xy = l47.start)
                elif (elem.kind == 'Current Dependent Source'):
                    S5 = d.add(e.SOURCE_CONT_I, d='right', label=str(elem.a)+elem.dtype+elem.dposition+' + '+str(elem.b), xy = l47.start)
                l47.color = 'none'
                if (elem.kind == 'Wire'):
                    # l47.color = 'black'
                    l47 = d.add(e.LINE, d='right', xy = d4.end, color='black')
            elif elem.position == '74':
                if (elem.kind == 'Resistor'):
                    R5 = d.add(e.RES, d='left', label=str(elem.value)+'$\Omega$', xy = l47.end)
                elif (elem.kind == 'Capacitor'):
                    R1 = d.add(e.CAP, d='left', label=str(elem.value)+'F', xy = l47.end)
                elif (elem.kind == 'Inductor'):
                    R1 = d.add(e.INDUCTOR, d='left', label=str(elem.value)+'H', xy = l47.end)
                elif (elem.kind == 'Voltage Independent Source'):
                    S5 = d.add(e.SOURCE_V, d='left', label=str(elem.value)+'V', xy = l47.end)
                elif (elem.kind == 'Current Independent Source'):
                    S5 = d.add(e.SOURCE_I, d='left', label=str(elem.value)+'A', xy = l47.end)
                elif (elem.kind == 'Voltage Dependent Source'):
                    S5 = d.add(e.SOURCE_CONT_V, d='left', label=str(elem.a)+elem.dtype+elem.dposition+' + '+str(elem.b), xy = l47.end)
                elif (elem.kind == 'Current Dependent Source'):
                    S5 = d.add(e.SOURCE_CONT_I, d='left', label=str(elem.a)+elem.dtype+elem.dposition+' + '+str(elem.b), xy = l47.end)
                l47.color = 'none'
                if (elem.kind == 'Wire'):
                    # l47.color = 'black'
                    l47 = d.add(e.LINE, d='right', xy = d4.end, color='black')
            elif elem.position == '45':
                if (elem.kind == 'Resistor'):
                    R6 = d.add(e.RES, d='down', label=str(elem.value)+'$\Omega$', xy = l45.start)
                elif (elem.kind == 'Capacitor'):
                    R1 = d.add(e.CAP, d='down', label=str(elem.value)+'F', xy = l45.start)
                elif (elem.kind == 'Inductor'):
                    R1 = d.add(e.INDUCTOR, d='down', label=str(elem.value)+'H', xy = l45.start)
                elif (elem.kind == 'Voltage Independent Source'):
                    S6 = d.add(e.SOURCE_V, d='down', label=str(elem.value)+'V', xy = l45.start)
                elif (elem.kind == 'Current Independent Source'):
                    S6 = d.add(e.SOURCE_I, d='down', label=str(elem.value)+'A', xy = l45.start)
                elif (elem.kind == 'Voltage Dependent Source'):
                    S6 = d.add(e.SOURCE_CONT_V, d='down', label=str(elem.a)+elem.dtype+elem.dposition+' + '+str(elem.b), xy = l45.start)
                elif (elem.kind == 'Current Dependent Source'):
                    S6 = d.add(e.SOURCE_CONT_I, d='down', label=str(elem.a)+elem.dtype+elem.dposition+' + '+str(elem.b), xy = l45.start)
                l45.color = 'none'
                if (elem.kind == 'Wire'):
                    # l45.color = 'black'
                    l45 = d.add(e.LINE, d='down', xy = d4.end, color='black')
            elif elem.position == '54':
                if (elem.kind == 'Resistor'):
                    R6 = d.add(e.RES, d='up', label=str(elem.value)+'$\Omega$', xy = l45.end)
                elif (elem.kind == 'Capacitor'):
                    R1 = d.add(e.CAP, d='up', label=str(elem.value)+'F', xy = l45.end)
                elif (elem.kind == 'Inductor'):
                    R1 = d.add(e.INDUCTOR, d='up', label=str(elem.value)+'H', xy = l45.end)
                elif (elem.kind == 'Voltage Independent Source'):
                    S6 = d.add(e.SOURCE_V, d='up', label=str(elem.value)+'V', xy = l45.end)
                elif (elem.kind == 'Current Independent Source'):
                    S6 = d.add(e.SOURCE_I, d='up', label=str(elem.value)+'A', xy = l45.end)
                elif (elem.kind == 'Voltage Dependent Source'):
                    S6 = d.add(e.SOURCE_CONT_V, d='up', label=str(elem.a)+elem.dtype+elem.dposition+' + '+str(elem.b), xy = l45.end)
                elif (elem.kind == 'Current Dependent Source'):
                    S6 = d.add(e.SOURCE_CONT_I, d='up', label=str(elem.a)+elem.dtype+elem.dposition+' + '+str(elem.b), xy = l45.end)
                l45.color = 'none'
                if (elem.kind == 'Wire'):
                    # l45.color = 'black'
                    l45 = d.add(e.LINE, d='down', xy = d4.end, color='black')
            elif elem.position == '56':
                if (elem.kind == 'Resistor'):
                    R7 = d.add(e.RES, d='down', label=str(elem.value)+'$\Omega$', xy = l56.start)
                elif (elem.kind == 'Capacitor'):
                    R1 = d.add(e.CAP, d='down', label=str(elem.value)+'F', xy = l56.start)
                elif (elem.kind == 'Inductor'):
                    R1 = d.add(e.INDUCTOR, d='down', label=str(elem.value)+'H', xy = l56.start)
                elif (elem.kind == 'Voltage Independent Source'):
                    S7 = d.add(e.SOURCE_V, d='down', label=str(elem.value)+'V', xy = l56.start)
                elif (elem.kind == 'Current Independent Source'):
                    S7 = d.add(e.SOURCE_I, d='down', label=str(elem.value)+'A', xy = l56.start)
                elif (elem.kind == 'Voltage Dependent Source'):
                    S7 = d.add(e.SOURCE_CONT_V, d='down', label=str(elem.a)+elem.dtype+elem.dposition+' + '+str(elem.b), xy = l56.start)
                elif (elem.kind == 'Current Dependent Source'):
                    S7 = d.add(e.SOURCE_CONT_I, d='down', label=str(elem.a)+elem.dtype+elem.dposition+' + '+str(elem.b), xy = l56.start)
                l56.color = 'none'
                if (elem.kind == 'Wire'):
                    # l56.color = 'black'
                    l56 = d.add(e.LINE, d='down', xy = d5.end, color='black')
            elif elem.position == '65':
                if (elem.kind == 'Resistor'):
                    R7 = d.add(e.RES, d='up', label=str(elem.value)+'$\Omega$', xy = l56.end)
                elif (elem.kind == 'Capacitor'):
                    R1 = d.add(e.CAP, d='up', label=str(elem.value)+'F', xy = l56.end)
                elif (elem.kind == 'Inductor'):
                    R1 = d.add(e.INDUCTOR, d='up', label=str(elem.value)+'H', xy = l56.end)
                elif (elem.kind == 'Voltage Independent Source'):
                    S7 = d.add(e.SOURCE_V, d='up', label=str(elem.value)+'V', xy = l56.end)
                elif (elem.kind == 'Current Independent Source'):
                    S7 = d.add(e.SOURCE_I, d='up', label=str(elem.value)+'A', xy = l56.end)
                elif (elem.kind == 'Voltage Dependent Source'):
                    S7 = d.add(e.SOURCE_CONT_V, d='up', label=str(elem.a)+elem.dtype+elem.dposition+' + '+str(elem.b), xy = l56.end)
                elif (elem.kind == 'Current Dependent Source'):
                    S7 = d.add(e.SOURCE_CONT_I, d='up', label=str(elem.a)+elem.dtype+elem.dposition+' + '+str(elem.b), xy = l56.end)
                l56.color = 'none'
                if (elem.kind == 'Wire'):
                    # l56.color = 'black'
                    l56 = d.add(e.LINE, d='down', xy = d5.end, color='black')
            elif elem.position == '78':
                if (elem.kind == 'Resistor'):
                    R8 = d.add(e.RES, d='down', label=str(elem.value)+'$\Omega$', xy = l78.start)
                elif (elem.kind == 'Capacitor'):
                    R1 = d.add(e.CAP, d='down', label=str(elem.value)+'F', xy = l78.start)
                elif (elem.kind == 'Inductor'):
                    R1 = d.add(e.INDUCTOR, d='down', label=str(elem.value)+'H', xy = l78.start)
                elif (elem.kind == 'Voltage Independent Source'):
                    S8 = d.add(e.SOURCE_V, d='down', label=str(elem.value)+'V', xy = l78.start)
                elif (elem.kind == 'Current Independent Source'):
                    S8 = d.add(e.SOURCE_I, d='down', label=str(elem.value)+'A', xy = l78.start)
                elif (elem.kind == 'Voltage Dependent Source'):
                    S8 = d.add(e.SOURCE_CONT_V, d='down', label=str(elem.a)+elem.dtype+elem.dposition+' + '+str(elem.b), xy = l78.start)
                elif (elem.kind == 'Current Dependent Source'):
                    S8 = d.add(e.SOURCE_CONT_I, d='down', label=str(elem.a)+elem.dtype+elem.dposition+' + '+str(elem.b), xy = l78.start)
                l78.color = 'none'
                if (elem.kind == 'Wire'):
                    # l78.color = 'black'
                    l78 = d.add(e.LINE, d='down', xy = d7.end, color='black')
            elif elem.position == '87':
                if (elem.kind == 'Resistor'):
                    R8 = d.add(e.RES, d='up', label=str(elem.value)+'$\Omega$', xy = l78.end)
                elif (elem.kind == 'Capacitor'):
                    R1 = d.add(e.CAP, d='up', label=str(elem.value)+'F', xy = l78.end)
                elif (elem.kind == 'Inductor'):
                    R1 = d.add(e.INDUCTOR, d='up', label=str(elem.value)+'H', xy = l78.end)
                elif (elem.kind == 'Voltage Independent Source'):
                    S8 = d.add(e.SOURCE_V, d='up', label=str(elem.value)+'V', xy = l78.end)
                elif (elem.kind == 'Current Independent Source'):
                    S8 = d.add(e.SOURCE_I, d='up', label=str(elem.value)+'A', xy = l78.end)
                elif (elem.kind == 'Voltage Dependent Source'):
                    S8 = d.add(e.SOURCE_CONT_V, d='up', label=str(elem.a)+elem.dtype+elem.dposition+' + '+str(elem.b), xy = l78.end)
                elif (elem.kind == 'Current Dependent Source'):
                    S8 = d.add(e.SOURCE_CONT_I, d='up', label=str(elem.a)+elem.dtype+elem.dposition+' + '+str(elem.b), xy = l78.end)
                l78.color = 'none'
                if (elem.kind == 'Wire'):
                    # l78.color = 'black'
                    l78 = d.add(e.LINE, d='down', xy = d7.end, color='black')
            elif elem.position == '36':
                if (elem.kind == 'Resistor'):
                    R9 = d.add(e.RES, d='right', label=str(elem.value)+'$\Omega$', xy = l36.start)
                elif (elem.kind == 'Capacitor'):
                    R1 = d.add(e.CAP, d='right', label=str(elem.value)+'F', xy = l36.start)
                elif (elem.kind == 'Inductor'):
                    R1 = d.add(e.INDUCTOR, d='right', label=str(elem.value)+'H', xy = l36.start)
                elif (elem.kind == 'Voltage Independent Source'):
                    S9 = d.add(e.SOURCE_V, d='right', label=str(elem.value)+'V', xy = l36.start)
                elif (elem.kind == 'Current Independent Source'):
                    S9 = d.add(e.SOURCE_I, d='right', label=str(elem.value)+'A', xy = l36.start)
                elif (elem.kind == 'Voltage Dependent Source'):
                    S9 = d.add(e.SOURCE_CONT_V, d='right', label=str(elem.value)+'V', xy = l36.start)
                elif (elem.kind == 'Current Dependent Source'):
                    S9 = d.add(e.SOURCE_CONT_I, d='right', label=str(elem.value)+'A', xy = l36.start)
                l36.color = 'none'
                if (elem.kind == 'Wire'):
                    # l36.color = 'black'
                    l36 = d.add(e.LINE, d='right', xy = d3.end, color='black')
            elif elem.position == '63':
                if (elem.kind == 'Resistor'):
                    R9 = d.add(e.RES, d='left', label=str(elem.value)+'$\Omega$', xy = l36.end)
                elif (elem.kind == 'Capacitor'):
                    R1 = d.add(e.CAP, d='left', label=str(elem.value)+'F', xy = l36.end)
                elif (elem.kind == 'Inductor'):
                    R1 = d.add(e.INDUCTOR, d='left', label=str(elem.value)+'H', xy = l36.end)
                elif (elem.kind == 'Voltage Independent Source'):
                    S9 = d.add(e.SOURCE_V, d='left', label=str(elem.value)+'V', xy = l36.end)
                elif (elem.kind == 'Current Independent Source'):
                    S9 = d.add(e.SOURCE_I, d='left', label=str(elem.value)+'A', xy = l36.end)
                elif (elem.kind == 'Voltage Dependent Source'):
                    S9 = d.add(e.SOURCE_CONT_V, d='left', label=str(elem.a)+elem.dtype+elem.dposition+' + '+str(elem.b), xy = l36.end)
                elif (elem.kind == 'Current Dependent Source'):
                    S9 = d.add(e.SOURCE_CONT_I, d='left', label=str(elem.a)+elem.dtype+elem.dposition+' + '+str(elem.b), xy = l36.end)
                l36.color = 'none'
                if (elem.kind == 'Wire'):
                    # l36.color = 'black'
                    l36 = d.add(e.LINE, d='right', xy = d3.end, color='black')
            elif elem.position == '69':
                if (elem.kind == 'Resistor'):
                    R10 = d.add(e.RES, d='right', label=str(elem.value)+'$\Omega$', xy = l69.start)
                elif (elem.kind == 'Capacitor'):
                    R1 = d.add(e.CAP, d='right', label=str(elem.value)+'F', xy = l69.start)
                elif (elem.kind == 'Inductor'):
                    R1 = d.add(e.INDUCTOR, d='right', label=str(elem.value)+'H', xy = l69.start)
                elif (elem.kind == 'Voltage Independent Source'):
                    S10 = d.add(e.SOURCE_V, d='right', label=str(elem.value)+'V', xy = l69.start)
                elif (elem.kind == 'Current Independent Source'):
                    S10 = d.add(e.SOURCE_I, d='right', label=str(elem.value)+'A', xy = l69.start)
                elif (elem.kind == 'Voltage Dependent Source'):
                    S10 = d.add(e.SOURCE_CONT_V, d='right', label=str(elem.a)+elem.dtype+elem.dposition+' + '+str(elem.b), xy = l69.start)
                elif (elem.kind == 'Current Dependent Source'):
                    S10 = d.add(e.SOURCE_CONT_I, d='right', label=str(elem.a)+elem.dtype+elem.dposition+' + '+str(elem.b), xy = l69.start)
                l69.color = 'none'
                if (elem.kind == 'Wire'):
                    # l69.color = 'black'
                    l69 = d.add(e.LINE, d='right', xy = d6.end, color='black')
            elif elem.position == '96':
                if (elem.kind == 'Resistor'):
                    R10 = d.add(e.RES, d='left', label=str(elem.value)+'$\Omega$', xy = l69.end)
                elif (elem.kind == 'Capacitor'):
                    R1 = d.add(e.CAP, d='left', label=str(elem.value)+'F', xy = l69.end)
                elif (elem.kind == 'Inductor'):
                    R1 = d.add(e.INDUCTOR, d='left', label=str(elem.value)+'H', xy = l69.end)
                elif (elem.kind == 'Voltage Independent Source'):
                    S10 = d.add(e.SOURCE_V, d='left', label=str(elem.value)+'V', xy = l69.end)
                elif (elem.kind == 'Current Independent Source'):
                    S10 = d.add(e.SOURCE_I, d='left', label=str(elem.value)+'A', xy = l69.end)
                elif (elem.kind == 'Voltage Dependent Source'):
                    S10 = d.add(e.SOURCE_CONT_V, d='left', label=str(elem.a)+elem.dtype+elem.dposition+' + '+str(elem.b), xy = l69.end)
                elif (elem.kind == 'Current Dependent Source'):
                    S10 = d.add(e.SOURCE_CONT_I, d='left', label=str(elem.a)+elem.dtype+elem.dposition+' + '+str(elem.b), xy = l69.end)
                l69.color = 'none'
                if (elem.kind == 'Wire'):
                    l69.color = 'black'
                    l69 = d.add(e.LINE, d='right', xy = d6.end, color='black')
            elif elem.position == '89':
                if (elem.kind == 'Resistor'):
                    R11 = d.add(e.RES, d='down', label=str(elem.value)+'$\Omega$', xy = l89.start)
                elif (elem.kind == 'Capacitor'):
                    R1 = d.add(e.CAP, d='down', label=str(elem.value)+'F', xy = l89.start)
                elif (elem.kind == 'Inductor'):
                    R1 = d.add(e.INDUCTOR, d='down', label=str(elem.value)+'H', xy = l89.start)
                elif (elem.kind == 'Voltage Independent Source'):
                    S11 = d.add(e.SOURCE_V, d='down', label=str(elem.value)+'V', xy = l89.start)
                elif (elem.kind == 'Current Independent Source'):
                    S11 = d.add(e.SOURCE_I, d='down', label=str(elem.value)+'A', xy = l89.start)
                elif (elem.kind == 'Voltage Dependent Source'):
                    S11 = d.add(e.SOURCE_CONT_V, d='down', label=str(elem.a)+elem.dtype+elem.dposition+' + '+str(elem.b), xy = l89.start)
                elif (elem.kind == 'Current Dependent Source'):
                    S11 = d.add(e.SOURCE_CONT_I, d='down', label=str(elem.a)+elem.dtype+elem.dposition+' + '+str(elem.b), xy = l89.start)
                l89.color = 'none'
                if (elem.kind == 'Wire'):
                    # l89.color = 'black'
                    l89 = d.add(e.LINE, d='down', xy = d8.end, color='black')
            elif elem.position == '98':
                if (elem.kind == 'Resistor'):
                    R11 = d.add(e.RES, d='up', label=str(elem.value)+'$\Omega$', xy = l89.end)
                elif (elem.kind == 'Capacitor'):
                    R1 = d.add(e.CAP, d='up', label=str(elem.value)+'F', xy = l89.end)
                elif (elem.kind == 'Inductor'):
                    R1 = d.add(e.INDUCTOR, d='up', label=str(elem.value)+'H', xy = l89.end)
                elif (elem.kind == 'Voltage Independent Source'):
                    S11 = d.add(e.SOURCE_V, d='up', label=str(elem.value)+'V', xy = l89.end)
                elif (elem.kind == 'Current Independent Source'):
                    S11 = d.add(e.SOURCE_I, d='up', label=str(elem.value)+'A', xy = l89.end)
                elif (elem.kind == 'Voltage Dependent Source'):
                    S11 = d.add(e.SOURCE_CONT_V, d='up', label=str(elem.a)+elem.dtype+elem.dposition+' + '+str(elem.b), xy = l89.end)
                elif (elem.kind == 'Current Dependent Source'):
                    S11 = d.add(e.SOURCE_CONT_I, d='up', label=str(elem.a)+elem.dtype+elem.dposition+' + '+str(elem.b), xy = l89.end)
                l89.color = 'none'
                if (elem.kind == 'Wire'):
                    # l89.color = 'black'
                    l89 = d.add(e.LINE, d='down', xy = d8.end, color='black')
            elif elem.position == '25':
                if (elem.kind == 'Resistor'):
                    R12 = d.add(e.RES, d='right', label=str(elem.value)+'$\Omega$', xy = l25.start)
                elif (elem.kind == 'Capacitor'):
                    R1 = d.add(e.CAP, d='right', label=str(elem.value)+'F', xy = l25.start)
                elif (elem.kind == 'Inductor'):
                    R1 = d.add(e.INDUCTOR, d='right', label=str(elem.value)+'H', xy = l25.start)
                elif (elem.kind == 'Voltage Independent Source'):
                    S12 = d.add(e.SOURCE_V, d='right', label=str(elem.value)+'V', xy = l25.start)
                elif (elem.kind == 'Current Independent Source'):
                    S12 = d.add(e.SOURCE_I, d='right', label=str(elem.value)+'A', xy = l25.start)
                elif (elem.kind == 'Voltage Dependent Source'):
                    S12 = d.add(e.SOURCE_CONT_V, d='right', label=str(elem.a)+elem.dtype+elem.dposition+' + '+str(elem.b), xy = l25.start)
                elif (elem.kind == 'Current Dependent Source'):
                    S12 = d.add(e.SOURCE_CONT_I, d='right', label=str(elem.a)+elem.dtype+elem.dposition+' + '+str(elem.b), xy = l25.start)
                l25.color = 'none'
                if (elem.kind == 'Wire'):
                    # l25.color = 'black'
                    l25 = d.add(e.LINE, d='right', xy = d2.end, color='black')
            elif elem.position == '52':
                if (elem.kind == 'Resistor'):
                    R12 = d.add(e.RES, d='left', label=str(elem.value)+'$\Omega$', xy = l25.end)
                elif (elem.kind == 'Capacitor'):
                    R1 = d.add(e.CAP, d='left', label=str(elem.value)+'F', xy = l25.end)
                elif (elem.kind == 'Inductor'):
                    R1 = d.add(e.INDUCTOR, d='left', label=str(elem.value)+'H', xy = l25.end)
                elif (elem.kind == 'Voltage Independent Source'):
                    S12 = d.add(e.SOURCE_V, d='left', label=str(elem.value)+'V', xy = l25.end)
                elif (elem.kind == 'Current Independent Source'):
                    S12 = d.add(e.SOURCE_I, d='left', label=str(elem.value)+'A', xy = l25.end)
                elif (elem.kind == 'Voltage Dependent Source'):
                    S12 = d.add(e.SOURCE_CONT_V, d='left', label=str(elem.a)+elem.dtype+elem.dposition+' + '+str(elem.b), xy = l25.end)
                elif (elem.kind == 'Current Dependent Source'):
                    S12 = d.add(e.SOURCE_CONT_I, d='left', label=str(elem.a)+elem.dtype+elem.dposition+' + '+str(elem.b), xy = l25.end)
                l25.color = 'none'
                if (elem.kind == 'Wire'):
                    # l25.color = 'black'
                    l25 = d.add(e.LINE, d='right', xy = d2.end, color='black')
        d.draw()

    def add_element(self, kind, left_pos, right_pos, value = 0,
            dleft_pos = None, dright_pos = None, dtype = None, a = None, b = None):
        position = left_pos + right_pos
        if (kind == 'Voltage Dependent Source' or kind == 'Current Dependent Source'):
            position2 = dleft_pos + dright_pos
            elem = element(kind, position, 0, position2, dtype, a, b)
        elif (kind == "Resistor" or kind == "Voltage Independent Source" or
                kind == "Current Independent Source" or kind == "Capacitor" or kind == "Inductor"):
            elem = element(kind, position, value)
        else:
            elem = element(kind, position)
        self.elements.append(elem)

    def solve_circuit(self):
        mycircuit = circuit()
        mycircuit.addR('R0', 0, 6, 0)
        for elem in self.elements:
            if elem.kind == "Wire":
                mycircuit.addR('R'+ elem.position, int(elem.position[0]), int(elem.position[1]), 0)

            elif elem.kind == "Resistor":
                mycircuit.addR('R'+ elem.position, int(elem.position[0]), int(elem.position[1]), elem.value)

            elif elem.kind == "Voltage Independent Source":
                mycircuit.addV('V'+ elem.position, int(elem.position[0]), int(elem.position[1]), elem.value)

            elif elem.kind == "Current Independent Source":
                mycircuit.addI('I'+ elem.position, int(elem.position[0]), int(elem.position[1]), elem.value)

            elif elem.kind == "Voltage Dependent Source":
                if elem.dtype == "V":
                    mycircuit.addVM('VM'+ elem.dposition, int(elem.dposition[0]), int(elem.dposition[1]))
                    mycircuit.addCVS('VD'+ elem.position, int(elem.position[0]), int(elem.position[1]), 'VM'+ elem.dposition, elem.a)
                else:
                    mycircuit.addIM('IM'+ elem.dposition, int(elem.dposition[0]), int(elem.dposition[1]))
                    mycircuit.addCVS('VD'+ elem.position, int(elem.position[0]), int(elem.position[1]), 'IM'+ elem.dposition, elem.a)

                if  elem.b != 0:
                    mycircuit.addV('V'+ elem.position, int(elem.position[0]), int(elem.position[1]), elem.b)

            elif elem.kind == "Current Dependent Source":
                if elem.dtype == "V":
                    mycircuit.addVM('VM'+ elem.dposition, int(elem.dposition[0]), int(elem.dposition[1]))
                    mycircuit.addCIS('VD'+ elem.position, int(elem.position[0]), int(elem.position[1]), 'VM'+ elem.dposition, elem.a)
                else:
                    mycircuit.addIM('IM'+ elem.dposition, int(elem.dposition[0]), int(elem.dposition[1]))
                    mycircuit.addCIS('VD'+ elem.position, int(elem.position[0]), int(elem.position[1]), 'IM'+ elem.dposition, elem.a)

                if  elem.b != 0:
                    mycircuit.addI('I'+ elem.position, int(elem.position[0]), int(elem.position[1]), elem.b)

            # Bonus part
            elif elem.kind == "Capacitor":
                mycircuit.addC('C'+ elem.position, int(elem.position[0]), int(elem.position[1]), elem.value)

            elif elem.kind == "Inductor":
                mycircuit.addL('L'+ elem.position, int(elem.position[0]), int(elem.position[1]), elem.value)

        self.results = mycircuit.solve()
        return self.results


verbose = True

# example of how to use:
# if __name__ == '__main__':

    # verbose = False

    # mycircuit = circuit()
    # mycircuit.add_element(kind = "Voltage Independent Source", left_pos = "1", right_pos = "2", value = 10)
    # mycircuit.add_element(kind = "Resistor", left_pos = "1", right_pos = "4", value = 5)
    # mycircuit.add_element(kind = "Wire", left_pos = "2", right_pos = "5")
    # mycircuit.add_element(kind = "Wire", left_pos = "4", right_pos = "5")
    # mycircuit.add_element(kind = "Wire", left_pos = "5", right_pos = "6")

    # results = mycircuit.solve_circuit()

    # for res in results:
    #     print(res, " = " , results[res])
