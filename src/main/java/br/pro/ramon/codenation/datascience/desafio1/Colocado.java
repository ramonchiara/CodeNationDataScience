package br.pro.ramon.codenation.datascience.desafio1;

import java.io.Serializable;
import javax.xml.bind.annotation.XmlElement;
import javax.xml.bind.annotation.XmlRootElement;
import javax.xml.bind.annotation.XmlTransient;
import javax.xml.bind.annotation.XmlType;
import org.apache.commons.csv.CSVRecord;

@XmlRootElement
@XmlType(propOrder = {"inscricao", "notaFinal"})
public class Colocado implements Serializable {

    private String inscricao;
    private double nota;

    protected Colocado() {
    }

    public Colocado(CSVRecord record) {
        this.inscricao = record.get("NU_INSCRICAO");
        this.nota = calculaNota(record);
    }

    private static double calculaNota(CSVRecord record) {
        double notaMatematica = getValue(record.get("NU_NOTA_MT"));
        double notaCienciasDaNatureza = getValue(record.get("NU_NOTA_CN"));
        double notaLinguagensECodigos = getValue(record.get("NU_NOTA_LC"));
        double notaCienciasHumanas = getValue(record.get("NU_NOTA_CH"));
        double notaRedacao = getValue(record.get("NU_NOTA_REDACAO"));

        double total = 0;
        total += 3.0 * notaMatematica;
        total += 2.0 * notaCienciasDaNatureza;
        total += 1.5 * notaLinguagensECodigos;
        total += 1.0 * notaCienciasHumanas;
        total += 3.0 * notaRedacao;
        return total / (3 + 2 + 1.5 + 1 + 3);
    }

    private static double getValue(String v) {
        return v.trim().isEmpty() ? 0.0 : Double.parseDouble(v);
    }

    @XmlElement(name = "NU_INSCRICAO")
    public String getInscricao() {
        return inscricao;
    }

    @XmlTransient
    public double getNota() {
        return nota;
    }

    @XmlElement(name = "NOTA_FINAL")
    public double getNotaFinal() {
        return new Double(String.format("%.1f", nota));
    }

}
