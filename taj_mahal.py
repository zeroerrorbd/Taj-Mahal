from graphics import *

def taj_mahal():
    win = GraphWin("My Window", 1100, 700)
    win.setBackground(color_rgb(0, 0 , 0))

#--------------------------------------------------Left Side Minar------------------------------------------------------
    ls_minar_1 = Polygon(Point(130, 650), Point(145, 350), Point(190, 350), Point(205, 650))
    ls_minar_1.setOutline(color_rgb(255, 255, 255))
    ls_minar_1.draw(win)

    ls_line_top_2 = Line(Point(365, 360), Point(365, 300))
    ls_line_top_2.setOutline(color_rgb(255, 255, 255))
    ls_line_top_2.draw(win)

    ls_cir_2 = Circle(Point(365, 360), 30)
    ls_cir_2.setOutline(color_rgb(255, 255, 255))
    ls_cir_2.setFill(color_rgb(0, 0, 0))
    ls_cir_2.draw(win)


    ls_minar_2 = Polygon(Point(340, 410), Point(390, 410), Point(390, 380), Point(340, 380))
    ls_minar_2.setOutline(color_rgb(255, 255, 255))
    ls_minar_2.setFill(color_rgb(0, 0, 0))
    ls_minar_2.draw(win)

    ls_small_cir_1_1 = Circle(Point(365, 320), 6)
    ls_small_cir_1_1.setOutline(color_rgb(255, 255, 255))
    ls_small_cir_1_1.setFill(color_rgb(0, 0, 0))
    ls_small_cir_1_1.draw(win)

    ls_small_cir_1_2 = Circle(Point(365, 307), 4)
    ls_small_cir_1_2.setOutline(color_rgb(255, 255, 255))
    ls_small_cir_1_2.setFill(color_rgb(0, 0, 0))
    ls_small_cir_1_2.draw(win)

    ls_poly_1 = Polygon(Point(135, 550), Point(125, 540), Point(140, 533), Point(150, 530), Point(175, 530),
                        Point(190, 533), Point(200, 535), Point(211, 540),
                        Point(200, 550))
    ls_poly_1.setOutline(color_rgb(255, 255, 255))
    ls_poly_1.setFill(color_rgb(0, 0, 0))
    ls_poly_1.draw(win)

    ls_poly_2 = Polygon(Point(135, 450), Point(125, 440), Point(140, 433), Point(150, 430), Point(175, 430),
                        Point(190, 433), Point(200, 435), Point(211, 440),
                        Point(200, 450))
    ls_poly_2.setOutline(color_rgb(255, 255, 255))
    ls_poly_2.setFill(color_rgb(0, 0, 0))
    ls_poly_2.draw(win)

    ls_rectan_1 = Polygon(Point(145, 350), Point(190, 350), Point(190, 320), Point(145, 320))
    ls_rectan_1.setOutline(color_rgb(255, 255, 255))
    ls_rectan_1.draw(win)


    ls_rectan_2 = Polygon(Point(335, 380), Point(395, 380), Point(395, 385), Point(335, 385))
    ls_rectan_2.setOutline(color_rgb(255, 255, 255))
    ls_rectan_2.setFill(color_rgb(0, 0, 0))
    ls_rectan_2.draw(win)


    ls_line_top = Line(Point(168, 285), Point(168, 210))
    ls_line_top.setOutline(color_rgb(255, 255, 255))
    ls_line_top.draw(win)

    ls_cir_1 = Circle(Point(168, 285), 35)
    ls_cir_1.setOutline(color_rgb(255, 255, 255))
    ls_cir_1.setFill(color_rgb(0, 0, 0))
    ls_cir_1.draw(win)

    ls_poly_top = Polygon(Point(145, 320), Point(142, 318), Point(140, 315), Point(138, 312), Point(145, 310),
                          Point(150, 309), Point(155, 308), Point(160, 307),
                          Point(165, 306), Point(170, 306), Point(185, 307), Point(190, 308), Point(195, 309),
                          Point(198, 310), Point(202, 315), Point(190, 320))
    ls_poly_top.setOutline(color_rgb(255, 255, 255))
    ls_poly_top.setFill(color_rgb(0, 0, 0))
    ls_poly_top.draw(win)

    ls_small_cir_1 = Circle(Point(168, 237), 7)
    ls_small_cir_1.setOutline(color_rgb(255, 255, 255))
    ls_small_cir_1.setFill(color_rgb(0, 0, 0))
    ls_small_cir_1.draw(win)

    ls_small_cir_2 = Circle(Point(168, 220), 5)
    ls_small_cir_2.setOutline(color_rgb(255, 255, 255))
    ls_small_cir_2.setFill(color_rgb(0, 0, 0))
    ls_small_cir_2.draw(win)

    ls_bold_piler_1 = Polygon(Point(300, 650), Point(300, 370), Point(305, 370), Point(305, 650))
    ls_bold_piler_1.setFill(color_rgb(255, 255, 255))
    ls_bold_piler_1.draw(win)

    ls_bold_piler_2 = Polygon(Point(238, 650), Point(238, 400), Point(243, 400), Point(243, 650))
    ls_bold_piler_2.setFill(color_rgb(255, 255, 255))
    ls_bold_piler_2.draw(win)

    ls_top_border = Polygon(Point(240, 450), Point(300, 410), Point(427, 410), Point(427, 440), Point(300, 440),
                              Point(240, 480))
    ls_top_border.setFill(color_rgb(215, 215, 215))
    ls_top_border.setOutline(color_rgb(255, 255, 255))
    ls_top_border.draw(win)

    ls_divided = Polygon(Point(240, 570), Point(300, 540), Point(430, 540), Point(300, 540))
    ls_divided.setOutline(color_rgb(255, 255, 255))
    ls_divided.draw(win)

#----------------------------------------------------Right Side Minar---------------------------------------------------

    rs_minar_1 = Polygon(Point(895, 650), Point(910, 350), Point(955, 350), Point(970, 650))
    rs_minar_1.setOutline(color_rgb(255,255,255))
    rs_minar_1.draw(win)

    rs_line_back_2 = Line(Point(735, 360), Point(735, 300))
    rs_line_back_2.setOutline(color_rgb(255, 255, 255))
    rs_line_back_2.draw(win)

    rs_small_cir_1_1 = Circle(Point(735, 320), 6)
    rs_small_cir_1_1.setOutline(color_rgb(255, 255, 255))
    rs_small_cir_1_1.setFill(color_rgb(0, 0, 0))
    rs_small_cir_1_1.draw(win)

    rs_small_cir_1_2 = Circle(Point(735, 307), 4)
    rs_small_cir_1_2.setOutline(color_rgb(255, 255, 255))
    rs_small_cir_1_2.setFill(color_rgb(0, 0, 0))
    rs_small_cir_1_2.draw(win)

    rs_cir_2 = Circle(Point(735, 360), 30)
    rs_cir_2.setOutline(color_rgb(255, 255, 255))
    rs_cir_2.setFill(color_rgb(0, 0, 0))
    rs_cir_2.draw(win)

    rs_minar_2 = Polygon(Point(710, 410), Point(760, 410), Point(760, 380), Point(710, 380))
    rs_minar_2.setOutline(color_rgb(255, 255, 255))
    rs_minar_2.setFill(color_rgb(0, 0, 0))
    rs_minar_2.draw(win)

    rs_rectan_2 = Polygon(Point(705, 380), Point(765, 380), Point(765, 385), Point(705, 385))
    rs_rectan_2.setOutline(color_rgb(255, 255, 255))
    rs_rectan_2.setFill(color_rgb(0, 0, 0))
    rs_rectan_2.draw(win)

    rs_poly_1 = Polygon(Point(965, 550), Point(975, 540), Point(960, 533), Point(950, 530), Point(925, 530),
                        Point(910, 533), Point(900, 535), Point(889, 540),
                        Point(900, 550))
    rs_poly_1.setOutline(color_rgb(255, 255, 255))
    rs_poly_1.setFill(color_rgb(0, 0, 0))
    rs_poly_1.draw(win)

    rs_poly_2 = Polygon(Point(905, 450), Point(895, 440), Point(910, 433), Point(945, 430), Point(950, 430),
                        Point(960, 433), Point(965, 435), Point(970, 440),
                        Point(960, 450))
    rs_poly_2.setOutline(color_rgb(255, 255, 255))
    rs_poly_2.setFill(color_rgb(0, 0, 0))
    rs_poly_2.draw(win)

    rs_rectan = Polygon(Point(910, 350), Point(955, 350), Point(955, 320), Point(910, 320))
    rs_rectan.setOutline(color_rgb(255, 255, 255))
    rs_rectan.draw(win)

    rs_line_top = Line(Point(933, 285), Point(933, 210))
    rs_line_top.setOutline(color_rgb(255, 255, 255))
    rs_line_top.draw(win)

    rs_cir_1 = Circle(Point(933, 285), 35)
    rs_cir_1.setOutline(color_rgb(255, 255, 255))
    rs_cir_1.setFill(color_rgb(0, 0, 0))
    rs_cir_1.draw(win)

    rs_poly_top = Polygon(Point(910, 320), Point(907, 318), Point(905, 315), Point(903, 312), Point(910, 310),
                          Point(915, 309), Point(920, 308), Point(925, 307),
                          Point(930, 306), Point(935, 306), Point(950, 307), Point(955, 308), Point(960, 309),
                          Point(963, 310), Point(967, 315), Point(955, 320))
    rs_poly_top.setOutline(color_rgb(255, 255, 255))
    rs_poly_top.setFill(color_rgb(0, 0, 0))
    rs_poly_top.draw(win)

    rs_small_cir_1 = Circle(Point(933, 237), 7)
    rs_small_cir_1.setOutline(color_rgb(255, 255, 255))
    rs_small_cir_1.setFill(color_rgb(0, 0, 0))
    rs_small_cir_1.draw(win)

    rs_small_cir_2 = Circle(Point(933, 220), 5)
    rs_small_cir_2.setOutline(color_rgb(255, 255, 255))
    rs_small_cir_2.setFill(color_rgb(0, 0, 0))
    rs_small_cir_2.draw(win)

#=====================================================Main Structure====================================================

#-----------------------------------------------------Inside Left-------------------------------------------------------
    ls_build = Polygon(Point(240, 650), Point(240, 450), Point(300, 410), Point(430, 410), Point(430, 650))
    ls_build.setOutline(color_rgb(255, 255, 255))
    ls_build.draw(win)

    ls_floor_white_win_1 = Polygon(Point(310, 533), Point(310, 447), Point(420, 447), Point(420, 533))
    ls_floor_white_win_1.setOutline(color_rgb(255, 255, 255))
    ls_floor_white_win_1.setFill(color_rgb(215, 215, 215))
    ls_floor_white_win_1.draw(win)

    ls_floor_black_win_1 = Polygon(Point(330, 530), Point(400, 530), Point(400, 480), Point(330, 480))
    ls_floor_black_win_1.setFill(color_rgb(0, 0, 0))
    ls_floor_black_win_1.draw(win)

    ls_floor_round_win_1 = Circle(Point(365, 485), 35)
    ls_floor_round_win_1.setFill(color_rgb(0, 0, 0))
    ls_floor_round_win_1.draw(win)

    ls_floor_white_win_2 = Polygon(Point(295, 534), Point(295, 451), Point(248, 482), Point(248, 557))
    ls_floor_white_win_2.setFill(color_rgb(255, 255, 255))
    ls_floor_white_win_2.draw(win)

    ls_floor_round_win_2 = Polygon(Point(255,543), Point(285,529), Point(285,497), Point(255,502))
    ls_floor_round_win_2.setFill(color_rgb(0, 0, 0))
    ls_floor_round_win_2.draw(win)

    ls_top_win_left_round = Circle(Point(270,500),15)
    ls_top_win_left_round.setFill(color_rgb(0,0,0))
    ls_top_win_left_round.draw(win)

    ground_floor_white_win_1 = Polygon(Point(310, 645), Point(310, 545), Point(420, 545), Point(420, 645))
    ground_floor_white_win_1.setOutline(color_rgb(255, 255, 255))
    ground_floor_white_win_1.setFill(color_rgb(215, 215, 215))
    ground_floor_white_win_1.draw(win)

    ground_floor_white_win_2 = Polygon(Point(295, 645), Point(295, 548), Point(248, 570), Point(248, 645))
    ground_floor_white_win_2.setFill(color_rgb(255, 255, 255))
    ground_floor_white_win_2.draw(win)

    ground_floor_black_win_2 = Rectangle(Point(255, 600), Point(285, 640))
    ground_floor_black_win_2.setFill(color_rgb(0, 0, 0))
    ground_floor_black_win_2.draw(win)

    ground_floor_round_win_2 = Circle(Point(270, 600), 15)
    ground_floor_round_win_2.setFill(color_rgb(0, 0, 0))
    ground_floor_round_win_2.draw(win)

    ground_floor_black_win_1 = Polygon(Point(330,642), Point(400,642), Point(400,592), Point(330,592))
    ground_floor_black_win_1.setFill(color_rgb(0,0,0))
    ground_floor_black_win_1.draw(win)

    ground_floor_round_win_1 = Circle(Point(365, 597), 35)
    ground_floor_round_win_1.setFill(color_rgb(0,0,0))
    ground_floor_round_win_1.draw(win)



#-------------------------------------------------Outside Main Structure------------------------------------------------

    hang_1 = Polygon(Point(550, 50), Point(545, 70), Point(540, 70), Point(535, 80), Point(530, 80), Point(525, 90),
                     Point(520, 90), Point(515, 100), Point(510, 100),
                     Point(505, 110), Point(500, 110), Point(495, 120), Point(490, 120), Point(485, 130),
                     Point(485, 130), Point(480, 140), Point(475, 140),
                     Point(470, 150), Point(465, 160), Point(460, 160), Point(460, 170), Point(455, 170),
                     Point(450, 180), Point(445, 180), Point(440, 140))
    hang_1.setOutline(color_rgb(255, 255, 255))
    hang_1.draw(win)

    hang_2 = Polygon(Point(550, 50), Point(555, 70), Point(560, 70), Point(565, 80), Point(570, 80), Point(575, 90),
                     Point(580, 90), Point(585, 100), Point(590, 100),
                     Point(595, 110), Point(600, 110), Point(605, 120), Point(610, 120), Point(615, 130),
                     Point(620, 130), Point(625, 140), Point(630, 140),
                     Point(635, 150), Point(640, 160), Point(645, 160), Point(650, 170), Point(655, 170),
                     Point(660, 180), Point(665, 180), Point(670, 150))
    hang_2.setOutline(color_rgb(255, 255, 255))
    hang_2.draw(win)

    mm_line_top = Line(Point(550, 265), Point(550, 20))
    mm_line_top.setOutline(color_rgb(255, 255, 255))
    mm_line_top.draw(win)

    mm_small_cir_1 = Circle(Point(550, 50), 8)
    mm_small_cir_1.setOutline(color_rgb(255, 255, 255))
    mm_small_cir_1.setFill(color_rgb(0, 0, 0))
    mm_small_cir_1.draw(win)

    mm_small_cir_2 = Circle(Point(550, 30), 5)
    mm_small_cir_2.setOutline(color_rgb(255, 255, 255))
    mm_small_cir_2.setFill(color_rgb(0, 0, 0))
    mm_small_cir_2.draw(win)

    mm_back_cir = Circle(Point(550, 235), 140)
    mm_back_cir.setFill(color_rgb(255, 255, 255))
    mm_back_cir.draw(win)

    mm_cir = Circle(Point(550, 260), 160)
    mm_cir.setOutline(color_rgb(255, 255, 255))
    mm_cir.setFill(color_rgb(0, 0, 0))
    mm_cir.draw(win)


#------------------------------------------------Inside Main Structure--------------------------------------------------


    ls_to_rs = Polygon(Point(430, 650), Point(430, 350), Point(670, 350), Point(670, 650))
    ls_to_rs.setOutline(color_rgb(255, 255, 255))
    ls_to_rs.setFill(color_rgb(0, 0, 0))
    ls_to_rs.draw(win)

    ls_to_rs_top = Polygon(Point(420, 350), Point(680, 350), Point(683, 347), Point(680, 345), Point(420, 345),
                           Point(417, 347))
    ls_to_rs_top.setOutline(color_rgb(255, 255, 255))
    ls_to_rs_top.setFill(color_rgb(255, 255, 255))
    ls_to_rs_top.draw(win)

    ls_bold_border_1 = Polygon(Point(425, 650), Point(425, 320), Point(430, 320), Point(430, 650))
    ls_bold_border_1.setFill(color_rgb(255, 255, 255))
    ls_bold_border_1.draw(win)

    rs_bold_border_1 = Polygon(Point(670, 650), Point(670, 320), Point(675, 320), Point(675, 650))
    rs_bold_border_1.setFill(color_rgb(255, 255, 255))
    rs_bold_border_1.draw(win)

    white_door = Polygon(Point(425, 650), Point(425, 610), Point(470, 610), Point(470, 390), Point(630, 390),
                         Point(630, 610), Point(675, 610), Point(675, 650))
    white_door.setFill(color_rgb(255, 255, 255))
    white_door.draw(win)

    door_thin_border = Polygon(Point(447,650), Point(447, 375), Point(653, 375), Point(653,650))
    door_thin_border.setOutline(color_rgb(255, 255, 255))
    door_thin_border.draw(win)

    inside_white_door = Polygon(Point(480,650), Point(480,400), Point(620,400), Point(620,650))
    inside_white_door.setFill(color_rgb(178,190,181))
    inside_white_door.draw(win)

    main_door = Polygon(Point(490, 649), Point(490, 490), Point(493, 485), Point(496, 480), Point(500, 475),
                         Point(503, 471), Point(506, 466), Point(510, 463),
                         Point(513, 460), Point(516, 457), Point(520, 453), Point(523, 450), Point(527, 446),
                         Point(535, 441), Point(540, 437), Point(545, 433),
                         Point(550, 429), Point(555, 433), Point(560, 437), Point(565, 441), Point(573, 446),
                         Point(577, 450), Point(580, 453), Point(584, 457),
                         Point(587, 460), Point(590, 463), Point(594, 466), Point(597, 471), Point(600, 475),
                         Point(604, 480), Point(607, 485), Point(610, 490),
                         Point(610, 649))
    main_door.setFill(color_rgb(0, 0, 0))
    main_door.draw(win)




#-----------------------------------------------------Inside Rigit------------------------------------------------------

    rs_bold_piler_1 = Polygon(Point(800, 650), Point(800, 370), Point(795, 370), Point(795, 650))
    rs_bold_piler_1.setFill(color_rgb(255, 255, 255))
    rs_bold_piler_1.draw(win)

    rs_bold_piler_2 = Polygon(Point(855, 650), Point(855, 400), Point(860, 400), Point(860, 650))
    rs_bold_piler_2.setFill(color_rgb(255, 255, 255))
    rs_bold_piler_2.draw(win)

    rs_build = Polygon(Point(855, 650), Point(855, 450), Point(800, 410), Point(670, 410), Point(670, 650))
    rs_build.setOutline(color_rgb(255, 255, 255))
    rs_build.draw(win)

    rs_top_border = Polygon(Point(855,450), Point(800,410), Point(674,410), Point(674,440), Point(800,440), Point(855,480))
    rs_top_border.setFill(color_rgb(215, 215, 215))
    rs_top_border.setOutline(color_rgb(255, 255, 255))
    rs_top_border.draw(win)

    rs_divided = Polygon(Point(855, 570), Point(795, 540), Point(674, 540), Point(795, 540))
    rs_divided.setOutline(color_rgb(255, 255, 255))
    rs_divided.draw(win)

    rs_floor_white_win_1 = Polygon(Point(680,533), Point(680,447), Point(790,447), Point(790,533))
    rs_floor_white_win_1.setOutline(color_rgb(255, 255, 255))
    rs_floor_white_win_1.setFill(color_rgb(215, 215, 215))
    rs_floor_white_win_1.draw(win)

    rs_floor_black_win_1 = Polygon(Point(700,530), Point(770,530), Point(770,480), Point(700,480))
    rs_floor_black_win_1.setFill(color_rgb(0,0,0))
    rs_floor_black_win_1.draw(win)

    rs_floor_round_1 = Circle(Point(735,485),35)
    rs_floor_round_1.setFill(color_rgb(0,0,0))
    rs_floor_round_1.draw(win)

    rs_floor_white_win_2 = Polygon(Point(804,450), Point(804,538), Point(849,560), Point(849,484))
    rs_floor_white_win_2.setFill(color_rgb(255,255,255))
    rs_floor_white_win_2.draw(win)

    rs__floor_round_2 = Circle(Point(825,500),15)
    rs__floor_round_2.setFill(color_rgb(0,0,0))
    rs__floor_round_2.draw(win)


    rs_floor_black_win_2 = Polygon(Point(840,543), Point(810,529), Point(810,497), Point(840,502))
    rs_floor_black_win_2.setFill(color_rgb(0,0,0))
    rs_floor_black_win_2.draw(win)

    ground_floor_white_win_1 = Polygon(Point(680, 645), Point(680, 545), Point(790, 545), Point(790, 645))
    ground_floor_white_win_1.setOutline(color_rgb(255, 255, 255))
    ground_floor_white_win_1.setFill(color_rgb(215, 215, 215))
    ground_floor_white_win_1.draw(win)

    ground_floor_white_win_2 = Polygon(Point(804,645), Point(804,548), Point(849,570), Point(849,645))
    ground_floor_white_win_2.setFill(color_rgb(255,255,255))
    ground_floor_white_win_2.draw(win)

    ground_floor_black_win_1 = Polygon(Point(700,642), Point(770,642), Point(770,592), Point(700,592))
    ground_floor_black_win_1.setFill(color_rgb(0,0,0))
    ground_floor_black_win_1.draw(win)

    ground_floor_round_1 = Circle(Point(735,597),35)
    ground_floor_round_1.setFill(color_rgb(0,0,0))
    ground_floor_round_1.draw(win)

    ground_floor_black_win_2 = Rectangle(Point(811,600), Point(841,640))
    ground_floor_black_win_2.setFill(color_rgb(0,0,0))
    ground_floor_black_win_2.draw(win)

    ground_floor_round_2 = Circle(Point(825.5,600),15)
    ground_floor_round_2.setFill(color_rgb(0,0,0))
    ground_floor_round_2.draw(win)


#===================================================Small Dome==========================================================

#--------------------------------------------------Left Side Dome-------------------------------------------------------

    ls_small_dome_cir_1 = Circle(Point(428, 315), 9)
    ls_small_dome_cir_1.setOutline(color_rgb(255, 255, 255))
    ls_small_dome_cir_1.setFill(color_rgb(0, 0, 0))
    ls_small_dome_cir_1.draw((win))

    ls_small_dome_1 = Rectangle(Point(418, 320), Point(438, 325))
    ls_small_dome_1.setOutline(color_rgb(255, 255, 255))
    ls_small_dome_1.setFill(color_rgb(0, 0, 0))
    ls_small_dome_1.draw(win)

    ls_small_dome_cir_2 = Circle(Point(302.5, 365), 9)
    ls_small_dome_cir_2.setOutline(color_rgb(255, 255, 255))
    ls_small_dome_cir_2.setFill(color_rgb(0, 0, 0))
    ls_small_dome_cir_2.draw(win)

    ls_small_dome_2 = Rectangle(Point(292, 370), Point(313, 375))
    ls_small_dome_2.setOutline(color_rgb(255, 255, 255))
    ls_small_dome_2.setFill(color_rgb(0, 0, 0))
    ls_small_dome_2.draw(win)

    ls_small_dome_cir_3 = Circle(Point(240, 390), 9)
    ls_small_dome_cir_3.setOutline(color_rgb(255, 255, 255))
    ls_small_dome_cir_3.setFill(color_rgb(0, 0, 0))
    ls_small_dome_cir_3.draw((win))

    ls_small_dome_3 = Rectangle(Point(230, 395), Point(250, 400))
    ls_small_dome_3.setOutline(color_rgb(255, 255, 255))
    ls_small_dome_3.setFill(color_rgb(0, 0, 0))
    ls_small_dome_3.draw(win)

#--------------------------------------------------Left Side Dome-------------------------------------------------------

    rs_small_dome_cir_1 = Circle(Point(672, 315), 9)
    rs_small_dome_cir_1.setOutline(color_rgb(255, 255, 255))
    rs_small_dome_cir_1.setFill(color_rgb(0, 0, 0))
    rs_small_dome_cir_1.draw(win)

    rs_small_dome_1 = Rectangle(Point(662, 320), Point(682, 325))
    rs_small_dome_1.setOutline(color_rgb(255, 255, 255))
    rs_small_dome_1.setFill(color_rgb(0, 0, 0))
    rs_small_dome_1.draw(win)

    rs_small_dome_cir_2 = Circle(Point(798, 365), 9)
    rs_small_dome_cir_2.setOutline(color_rgb(255, 255, 255))
    rs_small_dome_cir_2.setFill(color_rgb(0, 0, 0))
    rs_small_dome_cir_2.draw(win)

    rs_small_dome_2 = Rectangle(Point(788, 370), Point(808, 375))
    rs_small_dome_2.setOutline(color_rgb(255, 255, 255))
    rs_small_dome_2.setFill(color_rgb(0, 0, 0))
    rs_small_dome_2.draw(win)

    rs_small_dome_cir_3 = Circle(Point(857, 390), 9)
    rs_small_dome_cir_3.setOutline(color_rgb(255, 255, 255))
    rs_small_dome_cir_3.setFill(color_rgb(0, 0, 0))
    rs_small_dome_cir_3.draw(win)

    rs_small_dome_3 = Rectangle(Point(847, 395), Point(867, 400))
    rs_small_dome_3.setOutline(color_rgb(255, 255, 255))
    rs_small_dome_3.setFill(color_rgb(0, 0, 0))
    rs_small_dome_3.draw(win)

#----------------------------------------------------------Ground-------------------------------------------------------
    ground = Line(Point(1000, 650), Point(100, 650))
    ground.setOutline(color_rgb(255, 255, 255))
    ground.draw(win)



    win.getMouse()
    win.close()
taj_mahal()
