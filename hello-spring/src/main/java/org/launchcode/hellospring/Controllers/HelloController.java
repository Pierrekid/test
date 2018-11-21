package org.launchcode.hellospring.Controllers;


import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.ResponseBody;

import javax.servlet.http.HttpServletRequest;

@Controller
public class helloController {
    @RequestMapping(value = "")
    @ResponseBody
    public String index(HttpServletRequest request){

        String name = request.getParameter("name");
        if(name == null)
            { name = "phil";}

        return "Hello " + name;
    }
    @RequestMapping(value ="hello", method = RequestMethod.GET)
    @ResponseBody
    public String helloForm(){
        String html= "<form method = 'post'>" +
                "<input type ='text' name = 'name'/>" +
                "<input type ='submit' value ='Greet me!'/>" +
                "</form>";

        return html;
    }

    @RequestMapping(value = "hello", method = RequestMethod.POST)
    @ResponseBody
    public String helloPost(HttpServletRequest request){
        String name = request.getParameter("name");
                return "Hello " + name;

    }

    @RequestMapping(value = "hello/{name}")
    @ResponseBody
    public String hellowUrlSegment(@PathVariable String name){

        return "hello " + name;
    }

    @RequestMapping(value = "goodbye")
    public String goodbye(){
        return "redirect:/hello";
    }
}
