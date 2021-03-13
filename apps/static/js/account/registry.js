class ClassRegistry{
    static register(_name, _class){
        let globalRegistry = window.globalRegistry

        if(typeof globalRegistry === "undefined"){
            globalRegistry = {}
            window.globalRegistry = globalRegistry
        }

        let currentRegistry = globalRegistry[this.CLASS_KEY]

        if(typeof currentRegistry === "undefined"){
            currentRegistry = {}
            globalRegistry[this.CLASSKEY] = currentRegistry
        }
        currentRegistry[_name] = _class
    }

    static get(_name){
        return window.globalRegistry[this.CLASSKEY][_name]
    }

    static getAll(){
        return window.globalRegistry[this.CLASSKEY]
    }
}

class PageClassRegistry extends ClassRegistry {}
PageClassRegistry.CLASS_KEY = "PAGE_CLASS"   //STATIC VARIABLE

/*
window.globalRegistry = {"PAGE_CLASS" : {_name : _class}}
 */

export {
    ClassRegistry,
    PageClassRegistry
}