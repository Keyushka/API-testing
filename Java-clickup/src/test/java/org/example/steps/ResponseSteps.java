package org.example.steps;

import io.cucumber.java.en.Then;
import org.junit.Assert;

public class ResponseSteps extends BaseSteps {

    @Then("Check that status code is {int}")
    public void checkStatus(int status) {
        sharedTestData.getResponse().then().statusCode(status);
    }

    @Then("Check that the response contains the tag {string}")
    public void checkResponseContainsTag(String expectedTag) {
        String responseBody = sharedTestData.getResponse().getBody().asString();
        Assert.assertTrue("Response does not contain the expected tag", responseBody.contains(expectedTag));
    }
}
