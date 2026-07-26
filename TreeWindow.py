from Box import Box
from View import View
from Vec import Vec


class TreeWindow:

    def __init__(self, view: View, img_closed:str, img_opened:str, img_list_empty:str, pos:Vec):
        self.view = view
        self.img_closed = img_closed
        self.img_opened = img_opened
        self.img_list_empty = img_list_empty
        self.boxes = [Box(Vec(355,151),32,view),Box(Vec(429,151),32,view),Box(Vec(500,151),32,view),Box(Vec(586,151),32,view),Box(Vec(658,145),32,view),Box(Vec(735,151),32,view),Box(Vec(825,165),32,view),Box(Vec(958,185),32,view),Box(Vec(1024,172),32,view),Box(Vec(1094,190),32,view),Box(Vec(1186,184),32,view),Box(Vec(1281,179),32,view),Box(Vec(1358,165),32,view),Box(Vec(1431,174),32,view),Box(Vec(1500,170),32,view),
                      Box(Vec(412,321),43,view), Box(Vec(535,322),52,view),Box(Vec(665,363),50,view),Box(Vec(824,366),60,view),Box(Vec(977,340),53,view),Box(Vec(1175,325),48,view),Box(Vec(1311,300),55,view),Box(Vec(1422,366),63,view),
                      Box(Vec(429,708),52,view),Box(Vec(724,652),56,view),Box(Vec(1089,616),64,view),Box(Vec(1320,745),63,view),
                      Box(Vec(589,923),64,view),Box(Vec(1183,938),65,view),
                      Box(Vec(875,1088),90,view)]
        self.opened = False
        self.pos = pos
        self.width = 187 #width of the folder icon
        self.height = 193 #height of the folder icon

    def draw(self):
        if self.opened:
            self.view.draw_image(self.img_opened, self.pos)
        self.view.draw_image(self.img_closed, self.pos) # the folder is always showed