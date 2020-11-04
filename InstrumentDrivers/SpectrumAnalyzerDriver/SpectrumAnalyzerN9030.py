# -*- coding: utf-8 -*- 
'''
Created on 2015年5月14日

@author: SYH
'''

from .SpectrumAnalyzer import SpectrumAnalyzer

class SpectrumAnalyzerN9030A(SpectrumAnalyzer):
    '''
    classdocs
    '''
    def __init__(self,Addr):
        SpectrumAnalyzer.__init__(self,Addr)

    