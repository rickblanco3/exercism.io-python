class SpaceAge(object):
    planet_years = {
            'earth':31557600.0,
            'mercury':7600543.81992,
            'venus':19414149.052176,
            'mars':59354032.69008,
            'jupiter':374355659.124,
            'saturn':929292362.8848,
            'uranus':2651370019.3296,
            'neptune':5200418560.032
    }

    def __init__(self,seconds):
        self.seconds = seconds
        
    
    def __getattr__(self,name):
        if name[:3] == 'on_' and name[3:] in self.planet_years:
            def f():
                return round(self.seconds/self.planet_years[name[3:]],2)
            return f
        else:
            raise AttributeError("type object 'SpaceAge' has no attribute '%s'" % name) 

