var stats = {
    type: "GROUP",
name: "All Requests",
path: "",
pathFormatted: "group_missing-name--1146707516",
stats: {
    "name": "All Requests",
    "numberOfRequests": {
        "total": "500",
        "ok": "100",
        "ko": "400"
    },
    "minResponseTime": {
        "total": "92",
        "ok": "117",
        "ko": "92"
    },
    "maxResponseTime": {
        "total": "321",
        "ok": "197",
        "ko": "321"
    },
    "meanResponseTime": {
        "total": "111",
        "ok": "133",
        "ko": "105"
    },
    "standardDeviation": {
        "total": "19",
        "ok": "13",
        "ko": "17"
    },
    "percentiles1": {
        "total": "104",
        "ok": "130",
        "ko": "102"
    },
    "percentiles2": {
        "total": "119",
        "ok": "135",
        "ko": "108"
    },
    "percentiles3": {
        "total": "140",
        "ok": "156",
        "ko": "124"
    },
    "percentiles4": {
        "total": "164",
        "ok": "168",
        "ko": "148"
    },
    "group1": {
    "name": "t < 800 ms",
    "htmlName": "t < 800 ms",
    "count": 100,
    "percentage": 20.0
},
    "group2": {
    "name": "800 ms <= t < 1200 ms",
    "htmlName": "t >= 800 ms <br> t < 1200 ms",
    "count": 0,
    "percentage": 0.0
},
    "group3": {
    "name": "t >= 1200 ms",
    "htmlName": "t >= 1200 ms",
    "count": 0,
    "percentage": 0.0
},
    "group4": {
    "name": "failed",
    "htmlName": "failed",
    "count": 400,
    "percentage": 80.0
},
    "meanNumberOfRequestsPerSecond": {
        "total": "11.11",
        "ok": "2.22",
        "ko": "8.89"
    }
},
contents: {
"req_get-user-1918530133": {
        type: "REQUEST",
        name: "get user",
path: "get user",
pathFormatted: "req_get-user-1918530133",
stats: {
    "name": "get user",
    "numberOfRequests": {
        "total": "500",
        "ok": "100",
        "ko": "400"
    },
    "minResponseTime": {
        "total": "92",
        "ok": "117",
        "ko": "92"
    },
    "maxResponseTime": {
        "total": "321",
        "ok": "197",
        "ko": "321"
    },
    "meanResponseTime": {
        "total": "111",
        "ok": "133",
        "ko": "105"
    },
    "standardDeviation": {
        "total": "19",
        "ok": "13",
        "ko": "17"
    },
    "percentiles1": {
        "total": "104",
        "ok": "130",
        "ko": "102"
    },
    "percentiles2": {
        "total": "119",
        "ok": "135",
        "ko": "108"
    },
    "percentiles3": {
        "total": "140",
        "ok": "156",
        "ko": "124"
    },
    "percentiles4": {
        "total": "164",
        "ok": "168",
        "ko": "148"
    },
    "group1": {
    "name": "t < 800 ms",
    "htmlName": "t < 800 ms",
    "count": 100,
    "percentage": 20.0
},
    "group2": {
    "name": "800 ms <= t < 1200 ms",
    "htmlName": "t >= 800 ms <br> t < 1200 ms",
    "count": 0,
    "percentage": 0.0
},
    "group3": {
    "name": "t >= 1200 ms",
    "htmlName": "t >= 1200 ms",
    "count": 0,
    "percentage": 0.0
},
    "group4": {
    "name": "failed",
    "htmlName": "failed",
    "count": 400,
    "percentage": 80.0
},
    "meanNumberOfRequestsPerSecond": {
        "total": "11.11",
        "ok": "2.22",
        "ko": "8.89"
    }
}
    }
}

}

function fillStats(stat){
    $("#numberOfRequests").append(stat.numberOfRequests.total);
    $("#numberOfRequestsOK").append(stat.numberOfRequests.ok);
    $("#numberOfRequestsKO").append(stat.numberOfRequests.ko);

    $("#minResponseTime").append(stat.minResponseTime.total);
    $("#minResponseTimeOK").append(stat.minResponseTime.ok);
    $("#minResponseTimeKO").append(stat.minResponseTime.ko);

    $("#maxResponseTime").append(stat.maxResponseTime.total);
    $("#maxResponseTimeOK").append(stat.maxResponseTime.ok);
    $("#maxResponseTimeKO").append(stat.maxResponseTime.ko);

    $("#meanResponseTime").append(stat.meanResponseTime.total);
    $("#meanResponseTimeOK").append(stat.meanResponseTime.ok);
    $("#meanResponseTimeKO").append(stat.meanResponseTime.ko);

    $("#standardDeviation").append(stat.standardDeviation.total);
    $("#standardDeviationOK").append(stat.standardDeviation.ok);
    $("#standardDeviationKO").append(stat.standardDeviation.ko);

    $("#percentiles1").append(stat.percentiles1.total);
    $("#percentiles1OK").append(stat.percentiles1.ok);
    $("#percentiles1KO").append(stat.percentiles1.ko);

    $("#percentiles2").append(stat.percentiles2.total);
    $("#percentiles2OK").append(stat.percentiles2.ok);
    $("#percentiles2KO").append(stat.percentiles2.ko);

    $("#percentiles3").append(stat.percentiles3.total);
    $("#percentiles3OK").append(stat.percentiles3.ok);
    $("#percentiles3KO").append(stat.percentiles3.ko);

    $("#percentiles4").append(stat.percentiles4.total);
    $("#percentiles4OK").append(stat.percentiles4.ok);
    $("#percentiles4KO").append(stat.percentiles4.ko);

    $("#meanNumberOfRequestsPerSecond").append(stat.meanNumberOfRequestsPerSecond.total);
    $("#meanNumberOfRequestsPerSecondOK").append(stat.meanNumberOfRequestsPerSecond.ok);
    $("#meanNumberOfRequestsPerSecondKO").append(stat.meanNumberOfRequestsPerSecond.ko);
}
