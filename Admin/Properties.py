import flet as ft

def h4(txt):
    return {
        "size" : 20,
        "width" : 500,
        "weight" : ft.FontWeight.BOLD,
        "spans" : [ft.TextSpan(txt, ft.TextStyle(foreground=ft.Paint(
                                                    color=ft.colors.BLACK,
                                                    stroke_width=1,
                                                    stroke_join=ft.StrokeJoin.ROUND,
                                                    style=ft.PaintingStyle.STROKE,
                                                   
                                                ),weight=ft.FontWeight.BOLD))]
    }

def h5(txt):
    return {
        "size" : 15,
        "width" : 500,
        "weight" : ft.FontWeight.BOLD,
        "color" : ft.colors.WHITE,
        "spans" : [ft.TextSpan(txt, ft.TextStyle(shadow=ft.BoxShadow(2,5,ft.colors.BLACK,
                    blur_style=ft.ShadowBlurStyle.OUTER),color=ft.colors.BLACK, foreground=ft.Paint(color='#ffffff', stroke_width=0.1, stroke_join=ft.StrokeJoin.ROUND)))]
    
    }

def h1(txt):
    return {
        "size" : 22,
        "width" : 500,
        "weight" : ft.FontWeight.BOLD,
        "color" : ft.colors.WHITE,
        "spans" : [ft.TextSpan(txt, ft.TextStyle(shadow=ft.BoxShadow(2,5,ft.colors.BLACK,
                    blur_style=ft.ShadowBlurStyle.OUTER),color=ft.colors.BLACK, foreground=ft.Paint(color='#ffffff', stroke_width=0.1, stroke_join=ft.StrokeJoin.ROUND)))]
    }

def WebName():
    return {
        "value" : "Welcome back!",
        "size" : 20,
        "width" : 500, 
        "weight" : ft.FontWeight.BOLD,
        "color" : ft.colors.BLACK,

    }
    
def Title(txt):
    return {
       "size" : 40,
       "width" : 500,
       "weight" : ft.FontWeight.BOLD,
       "color" : '#ffb4fe',
       "spans" : [ft.TextSpan(txt, ft.TextStyle(shadow=ft.BoxShadow(2,5,ft.colors.BLACK,
                    blur_style=ft.ShadowBlurStyle.OUTER),color=ft.colors.BLACK, foreground=ft.Paint(color='#ffb4fe', stroke_width=0.1, stroke_join=ft.StrokeJoin.ROUND)))]
    }

def BG(): 
    return {
        "height" : 1600,
        "width" : 900,
        "bgcolor" : "ffffff",
        "offset" : ft.Offset(x=0, y=0),
        "expand" : True
    }
    
def MainButton(Y):
    return {
        "text" : f"{Y}",
        "width" : 100,
        "height" : 35,
        "style" : ft.ButtonStyle(color=ft.colors.WHITE),
        
    }

def Amount(amount, scale):
    return {
        "weight" : ft.FontWeight.BOLD, 
        "color" : ft.colors.WHITE, 
        "spans" : [ft.TextSpan(f"{amount}",ft.TextStyle(shadow=ft.BoxShadow(2,5,ft.colors.BLACK, blur_style=ft.ShadowBlurStyle.OUTER),color=ft.colors.BLACK,
                                                                        foreground=ft.Paint(color=ft.colors.WHITE, stroke_width=0.1, stroke_join=ft.StrokeJoin.ROUND)))],
        "size" : scale
    }
    
def C_Box():
    return {
        "width" : 200,
        "height" : 100,
        "gradient" : ft.LinearGradient(colors=['#ffb4fe', '#fbe5fe'], rotation=90),
        "shadow" : ft.BoxShadow(2,5,ft.colors.BLACK45),
        "border_radius" : ft.border_radius.all(20),
        "padding" : 10
      
    }
    
def Box_():
    return {
       "width" : 427,
       "height" : 165,
       "gradient" : ft.LinearGradient(colors=['#ffb4fe', '#fbe5fe'], rotation=90),
       "shadow" : ft.BoxShadow(2,5,ft.colors.BLACK45),
       "border_radius" : ft.border_radius.all(17),
       "border" : ft.border.all(1, ft.colors.BLACK),

    }    
    
def Infotxt(txt):
    return {
        "weight" : ft.FontWeight.BOLD, 
        "color" : ft.colors.WHITE, 
        "spans" : [ft.TextSpan(f"{txt}",ft.TextStyle(shadow=ft.BoxShadow(2,5,ft.colors.PINK_300, blur_style=ft.ShadowBlurStyle.OUTER),color=ft.colors.PINK_200,
                                                                        foreground=ft.Paint(color=ft.colors.WHITE, stroke_width=0.1, stroke_join=ft.StrokeJoin.ROUND)))],
        "size" : 20
    }
    
def Table():
    return {
        'bgcolor' : '#ffdbfe',
        'border_radius' : ft.border_radius.all(20),
        "horizontal_lines" : ft.BorderSide(2, '#f6b3ff'),
        "vertical_lines" : ft.BorderSide(2, '#f6b3ff'),
        "border" : ft.border.all(2, '#f6b3ff')
    }
    
def Labels(label): #TextFields Emails
    return{
        "value" : label,
        "border_radius" : 15,
        "border_color" : '#ff94fe',
        "col" : {'xs': 12, 'sm': 9, 'md': 11, 'lg': 9, 'xl': 5},
        "scale" : 1,
        "text_style" : ft.TextStyle(color=ft.colors.PINK_300),
        "focused_color" : ft.colors.PINK_200,
        "height" : 40
    }    
    
def Sub_(txt):
    return {
       "size" : 15,
       "text_align" : ft.TextAlign.CENTER,
       "width" : 80,
       "weight" : ft.FontWeight.BOLD,
       "color" : ft.colors.WHITE,
       "spans" : [ft.TextSpan(txt, ft.TextStyle(shadow=ft.BoxShadow(1,5,ft.colors.PINK_300,
                    blur_style=ft.ShadowBlurStyle.OUTER),color=ft.colors.PINK_200, foreground=ft.Paint(color=ft.colors.WHITE, stroke_width=0.1, stroke_join=ft.StrokeJoin.ROUND)))]
    }    
    
def Heading_(txt):
    return {
       "size" : 22,
       "text_align" : ft.TextAlign.CENTER,
       "width" : 500,
       "weight" : ft.FontWeight.BOLD,
       "color" : ft.colors.WHITE,
       "spans" : [ft.TextSpan(txt, ft.TextStyle(shadow=ft.BoxShadow(1,5,ft.colors.PINK_300,
                    blur_style=ft.ShadowBlurStyle.OUTER),color=ft.colors.PINK_200, foreground=ft.Paint(color=ft.colors.WHITE, stroke_width=0.1, stroke_join=ft.StrokeJoin.ROUND)))]
    }    

def Acpt_button():
    return {
        "height" : 22,
        "text" : "Accept",
        "style" : ft.ButtonStyle(color='#509c4e', bgcolor='#86ff82', shape=ft.RoundedRectangleBorder("roundedRectangle", 5)),
        "icon" : ft.icons.CHECK
    }

def Decl_button():
    return {
        "height" : 23,
        "text" : "Decline",
        "style" : ft.ButtonStyle(color='#ff3d4a', bgcolor='#ffa6ac', shape=ft.RoundedRectangleBorder("roundedRectangle", 5)),
        "icon" : ft.icons.DO_NOT_DISTURB_ALT
    }
    
def Main(txt):
        return {
        "weight" : ft.FontWeight.BOLD, 
        "color" : ft.colors.BLACK, 
        "size" : 25,
        "spans" : [ft.TextSpan(f"{txt}",ft.TextStyle(shadow=ft.BoxShadow(2,5,ft.colors.PINK_300, blur_style=ft.ShadowBlurStyle.OUTER),color=ft.colors.PINK_200,
                                                                        foreground=ft.Paint(color=ft.colors.WHITE, stroke_width=0.1, stroke_join=ft.StrokeJoin.ROUND)))],
    }

def SubText(txt):
    return {
        "weight" : ft.FontWeight.BOLD, 
        "color" : ft.colors.WHITE, 
        "spans" : [ft.TextSpan(f"{txt}",ft.TextStyle(shadow=ft.BoxShadow(2,5,ft.colors.BLACK, blur_style=ft.ShadowBlurStyle.OUTER),color=ft.colors.BLACK,
                                                                        foreground=ft.Paint(color=ft.colors.WHITE, stroke_width=0.1, stroke_join=ft.StrokeJoin.ROUND)))],
        "size" : 20
    }

def SubInfo(txt):
    return {
        "weight" : ft.FontWeight.BOLD, 
        "color" : ft.colors.WHITE, 
        "spans" : [ft.TextSpan(f"{txt}",ft.TextStyle(shadow=ft.BoxShadow(2,5,ft.colors.BLACK, blur_style=ft.ShadowBlurStyle.OUTER),color=ft.colors.BLACK,
                                                                        foreground=ft.Paint(color=ft.colors.WHITE, stroke_width=0.1, stroke_join=ft.StrokeJoin.ROUND)))],
        "size" : 15
    }
def PriceField():
    return {
        "height" : 40,
        "width" : 200,
        'border_width' : 3,
        "border_color" : '000000',
        "gradient" : ft.LinearGradient(colors=['#ffb4fe', '#fbe5fe']),
        "text_style" : ft.TextStyle(shadow=ft.BoxShadow(2,5,ft.colors.PINK_300, blur_style=ft.ShadowBlurStyle.OUTER),color=ft.colors.PINK_200,weight=ft.FontWeight.BOLD,
                                                                        foreground=ft.Paint(color=ft.colors.WHITE, stroke_width=0.1, stroke_join=ft.StrokeJoin.ROUND))
    }

def Proceed():
    return {
        "height" : 50,
        "width" : 200,
        "style" : ft.ButtonStyle(color='#509c4e', bgcolor='#86ff82', shape=ft.RoundedRectangleBorder("roundedRectangle", 5)),
        "icon" : ft.icons.CHECK
    }
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    