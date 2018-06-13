package br.pro.ramon.codenation.datascience.desafio1;

import java.io.Serializable;
import java.util.ArrayList;
import java.util.List;
import javax.xml.bind.annotation.XmlElement;
import javax.xml.bind.annotation.XmlRootElement;
import javax.xml.bind.annotation.XmlType;

@XmlRootElement
@XmlType(propOrder = {"token", "email", "answer"})
public class Envio implements Serializable {

    private String token = "b33ce0b52f2252786237a0ce80417dbfa954214c";
    private String email = "ramonchiara@gmail.com";
    private List<Colocado> answer = new ArrayList<>();

    protected Envio() {
    }

    public Envio(List<Colocado> answer) {
        this.answer = answer;
    }

    @XmlElement
    public String getToken() {
        return token;
    }

    @XmlElement
    public String getEmail() {
        return email;
    }

    @XmlElement
    public List<Colocado> getAnswer() {
        return answer;
    }

}
