#https://preslav.me/2018/12/20/dependency-injection-in-python/


#pip install dependency-injector
import dependency_injector.containers as containers
import dependency_injector.providers as providers



"""
There is one golden prerequisite for Dependency Injection and that is, Separation of Concerns. Put simply, group logic in separable units, and let these units work together, without any of them knowing much about the implementation details of the other. OOP calls such units classes, and FP, functions. The point is, units isolate common logic. Lets add to this the requirement that no unit explicitly instantiates the units it works with (dependencies). Instead, dependencies are passed upon the unit (injected), usually, during its instantiation.

So, DI is a fancy term for instantiating classes in a top-level module, and passing them as initializer arguments to one another:
"""

class Api:
    def fetch_remote_data(self):
        print('Api called')
        return 42


class BusinessLogic:
    def __init__(self, api: Api):
        self.api = api

    def do_stuff(self):
        api_result = self.api.fetch_remote_data()
        print(f'the api returned a result: {api_result}')
        # do something with the data and return a result



"""
The only modification I made, was adding an explicit type hint to the Api dependency. This will be used by the library to determine the right object to pass at instantiation.
"""




class Api:
    def fetch_remote_data(self):
        print('Api called')
        return 42


class BusinessLogic:
    def __init__(self, api: Api):
        self.api = api

    def do_stuff(self):
        api_result = self.api.fetch_remote_data()
        print(f'the api returned a result: {api_result}')
        # do something with the data and return a result




class Engine:
    """Example engine base class.

    Engine is a heart of every car. Engine is a very common term and could be
    implemented in very different ways.
    """


class GasolineEngine(Engine):
    """Gasoline engine."""


class DieselEngine(Engine):
    """Diesel engine."""


class ElectricEngine(Engine):
    """Electric engine."""


"""Dependency injection example, cars module."""


class Car:
    """Example car."""

    def __init__(self, engine):
        """Initialize instance."""
        self._engine = engine  # Engine is injected
        



class Engines(containers.DeclarativeContainer):
    """IoC container of engine providers."""

    gasoline = providers.Factory(GasolineEngine)

    diesel = providers.Factory(DieselEngine)

    electric = providers.Factory(ElectricEngine)


class Cars(containers.DeclarativeContainer):
    """IoC container of car providers."""

    gasoline = providers.Factory(Car,
                                 engine=Engines.gasoline)

    diesel = providers.Factory(Car,
                               engine=Engines.diesel)

    electric = providers.Factory(Car,
                                 engine=Engines.electric)

        
from injector import Module, singleton, provider

class AppModule(Module):

    @singleton
    @provider
    def provide_business_logic(self, api: Api) -> BusinessLogic:
        return BusinessLogic(api=api)

    @singleton
    @provider
    def provide_api(self) -> Api:
        # there is no complex logic in our case,
        # but you can use this method to hide the complexity of initial 
        configuration
        # e.g. when instantiating a particular DB connector.
        return Api()
    
# ---

if __name__ == '__main__':
    api = Api()
    logic = BusinessLogic(api=api)

    # ...
    print(logic.do_stuff())


    gasoline_car = Car(GasolineEngine())
    diesel_car = Car(DieselEngine())
    electric_car = Car(ElectricEngine())


    gasoline_car = Cars.gasoline()
    diesel_car = Cars.diesel()
    electric_car = Cars.electric()


    injector = Injector(AppModule())

    logic = injector.get(BusinessLogic)
    logic.do_stuff()
