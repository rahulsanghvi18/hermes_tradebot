import {PageClassRegistry} from "../../frontend/registry"

window.addEventListener("load", () => {
    let p = document.body.dataset.page;
    if(p){
        p = JSON.parse(p)
        p.forEach((key) => {
            let _class = PageClassRegistry.get(key)
            let $object = new _class(document.body)
            $object.setup()
        })
    }
})