package org.example.rest;

import io.restassured.http.ContentType;
import io.restassured.specification.RequestSpecification;
import net.serenitybdd.rest.SerenityRest;

public abstract class BaseRestClient {
    protected final String token = "pk_2144410100_UHSIC7AK5SLLZTOD067P1TI0QIXO1YGD";
    protected final String baseUrl = "https://api.clickup.com/api/v2";

    protected RequestSpecification requestSpec;

    public void setUpRestAssured(){
        this.requestSpec = SerenityRest.given()
                .baseUri(this.baseUrl)
                .header("Authorization", token)
                .header("Content-Type", "application/json")
                .header("Accept", "application/json");
               // .contentType(ContentType.JSON);
    }
}
