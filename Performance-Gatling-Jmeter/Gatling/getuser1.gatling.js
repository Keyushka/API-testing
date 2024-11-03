import {
    scenario,
    simulation,
    constantUsersPerSec,
    stressPeakUsers
} from "@gatling.io/core";
import { http } from "@gatling.io/http";

export default simulation((setUp) => {

    const httpProtocol = http
        .baseUrl("https://api.clickup.com/api/v2")
        .acceptHeader("application/json")
        .contentTypeHeader("application/json")
        .header("Authorization", token);


    const getUser = scenario("Get Authorized User")
        .exec(http("get user").get("/user"));

    setUp(
        getUser.injectOpen(
            // Навантаження 10 users/sec протягом 20 sec,
            constantUsersPerSec(10).during(20),
            // потім пікове навантаження 100 users/sec на 5 sec
            stressPeakUsers(100).during(5),
            // і ще 10 users/sec протягом 20 sec
            constantUsersPerSec(10).during(20)
        )
    ).protocols(httpProtocol);
});