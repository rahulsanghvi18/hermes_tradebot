import {BasePage} from "./base"
import {PageClassRegistry} from "../../frontend/registry"
import "bootstrap/dist/js/bootstrap.min"
import $ from "jquery"

class CommonPage extends BasePage{
    setup() {
        super.setup();
        $(".toast").toast("show");
    }
}

PageClassRegistry.register("CommonPage", CommonPage)

export{
    CommonPage
}
