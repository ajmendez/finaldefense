COLORS = {'Astrophysics':'blue',
           'Biophysics':'green',
           'Condensed Matter':'DarkRed',
           'Plasma Physics':'black',
           'High Energy':'OrangeRed',
           }

PHYS_GROUPS = {'Astrophysics':['Coil','Wolfe','Tytler','Griest','Fuller',
                               'Shu','Diamond','Paar','Norman','Rothschild',
                               'Keating',],
               'Biophysics':['Abarbanel','Dudko','Groisman','Jun',
                             'Kleinfeld','Schoetz','Di Ventra','Hwa',
                             'Wolynes','Onuchic','Song','Lauga','Nguyen',
                             'Holst','Sharpee','Kristan','Jiang'],
                'Condensed Matter':[
                            'Arovas','Di Ventra','Fogler','Fredkin',
                            'Hirsch','Levine','Sham','Suhl','Wu',
                            # Exp
                            'Basov','Barreiro','Berkowitz','Butov',
                            'Dynes','Goodkind','Maple','Schuller',
                            'Schultz','Shpyrko','Sinha','Smith',
                            'Tu','Fainman','Meyer','Lomakin','Liu'],
               'Plasma Physics':['Driscoll','Dubin',"O'Neil",'Surko','Continetti'],
               'High Energy':['Manohar','Grinstein','Intriligator','Jenkins',
                             'Kuti','Sharma','Wuerthwein','Yagil','Branson'],
               }


def get_research(name):
    for key,people in PHYS_GROUPS.iteritems():
        for person in people:
            if person in name:
                return key
