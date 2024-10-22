package org.example.steps;

import io.cucumber.java.en.Given;
import net.serenitybdd.rest.SerenityRest;
import org.json.JSONArray;
import org.json.JSONObject;

public class Template {

    String token = "pk_2144410100_UHSIC7AK5SLLZTOD067P1TI0QIXO1YGD";
    String baseURL = "https://api.clickup.com/api/v2";
    String space_id = "90121364847";

    @Given("Sent request to get space tags")
    public void getSpaceTags() {
        SerenityRest.given()
                .baseUri(baseURL)
                .header("Authorization", token)
                .header("Content-Type", "application/json")
                .when()
                .get("/space/"+ space_id + "/tag")
                .then()
                .statusCode(200);
    }

    @Given("Sent request to create space tag")
    public void createSpaceTags() {
        SerenityRest.given()
                .baseUri(baseURL)
                .header("Authorization", token)
                .header("Content-Type", "application/json")
                .when()
                .post("/space/"+ space_id + "/tag")
                .then()
                .statusCode(200);
    }


    @Given("Sent request to get list id")
    public void getListIdFromResponse() {
        String response =  SerenityRest.given()
                .baseUri(baseURL)
                .header("Authorization", token)
                .header("Content-Type", "application/json")
                .get("/folder/90122619398/list")
                .then()
                .extract()
                .body()
                .asString();
        JSONObject obj = new JSONObject(response);
        JSONArray listArray = obj.getJSONArray("lists");
        JSONObject list = listArray.getJSONObject(0);
        String id = list.getString("id");
        System.out.println(id);

    }
}
