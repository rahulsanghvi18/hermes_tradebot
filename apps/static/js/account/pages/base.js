export class BasePage{
    constructor($document) {
        this.document = $document
    }

    setup(){
        this.bindEvents()
        this.afterLoad()
    }

    bindEvents(){

    }

    afterLoad(){

    }
}