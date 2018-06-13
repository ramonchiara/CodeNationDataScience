package br.pro.ramon.codenation.datascience.desafio1;

import com.fasterxml.jackson.databind.ObjectMapper;
import com.fasterxml.jackson.databind.SerializationFeature;
import com.fasterxml.jackson.databind.type.TypeFactory;
import com.fasterxml.jackson.module.jaxb.JaxbAnnotationIntrospector;
import com.sun.jersey.api.client.Client;
import com.sun.jersey.api.client.ClientResponse;
import com.sun.jersey.api.client.WebResource;
import java.io.FileReader;
import java.io.IOException;
import java.io.Reader;
import java.util.List;
import java.util.Locale;
import java.util.stream.Collectors;
import javax.ws.rs.core.MediaType;
import javax.xml.bind.JAXBContext;
import javax.xml.bind.JAXBException;
import javax.xml.bind.Marshaller;
import org.apache.commons.csv.CSVFormat;
import org.apache.commons.csv.CSVParser;

public class Program {

    public static void main(String[] args) {
        Locale.setDefault(Locale.US);

        try (Reader in = new FileReader("train.csv")) {
            CSVParser records = CSVFormat.RFC4180.withFirstRecordAsHeader().parse(in);
            List<Colocado> colocados = records.getRecords().stream()
                    .map(r -> new Colocado(r))
                    .sorted((o1, o2) -> {
                        if (o1.getNota() < o2.getNota()) {
                            return 1;
                        } else if (o1.getNota() > o2.getNota()) {
                            return -1;
                        } else {
                            return o1.getInscricao().compareTo(o2.getInscricao());
                        }
                    })
                    .limit(20)
                    .collect(Collectors.toList());
            Envio envio = new Envio(colocados);

            JAXBContext ctx = JAXBContext.newInstance(Envio.class);
            Marshaller marshaller = ctx.createMarshaller();
            marshaller.setProperty(Marshaller.JAXB_FORMATTED_OUTPUT, true);
            // marshaller.marshal(envio, System.out);

            ObjectMapper mapper = new ObjectMapper();
            mapper.setAnnotationIntrospector(new JaxbAnnotationIntrospector(TypeFactory.defaultInstance()));
            mapper.enable(SerializationFeature.INDENT_OUTPUT);
            String payload = mapper.writeValueAsString(envio);
            System.out.println(payload);

            Client client = Client.create();
            WebResource resource = client.resource("https://api.codenation.com.br/v1/user/acceleration/data-science/challenge/enem-1/submit");
            ClientResponse response = resource.accept(MediaType.APPLICATION_JSON).post(ClientResponse.class, payload);
            String output = response.getEntity(String.class);
            System.out.println(output);
        } catch (IOException | JAXBException ex) {
            System.out.println("Erro: " + ex.getMessage());
        }
    }

}
