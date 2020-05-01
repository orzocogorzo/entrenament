# EXEMPLE 1
def quote (content):
    # --> aqui
    #   CONTENT = "La meva cita de torn"
    #   return '"La meva cita de torn"'
    return '"' + content + '"'
    
    
def author (fn):
    def _fn (content):
        # --> AQUI
        #    content = 'La meva cita de torn'
        #    return "Lucas García: " + 
        return "Lucas García: " + fn(content)
    
    return _fn


complete_quote = author(quote)

la_meva_cita = complete_quote("La meva cita de torn")

print(la_meva_cita) # --> 'Lucas García: "La meva cita de torn"'


# EXEMPLE 2
def author (fn):
    
    def _fn (content):
        return "Lucas García: " + fn(content)
    
    return _fn
    

@author
def quote (content):
    return '"' + content + '"'
    

la_meva_cita = quote("La meva cita")
print(la_meva_cita) # --> 'Lucas García: "La meva cita"'
    


# EXEMPLE 3
class App:

    def __init__ (self):
        self.request = "I'm a request object"
        self.my_routes = {}
        
    def route (self, route_defn):
        # AQUI
        # route_dfn = '/'"
        
        def middleware (fn):
            # AQUI
            # fn = index
            
            def _fn ():
                print("callback to route: " + route_defn)
                return fn(self.request)
                            
            self.my_routes[route_defn] = _fn
            return _fn
        
        return middleware
    
    
app = App()

print(app) --> {
    "request": "I'm a request",
    "my_routes": {},
    "route": fn
}


decorator = app.route("/")
@decorator
# @app.route("/")
def index (req):
    print(req)
    
    
app.run(debug=True)
    
    
    
    
    
    
    
    
