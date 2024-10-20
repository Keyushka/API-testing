import * as allure from "allure-js-commons"

Cypress.Commands.add('sentRequest', (method, url, payload) => {
    return cy.request({
        method: method,
        url: url,
        body: payload,
        failOnStatusCode: false,
        headers: {
            Authorization: Cypress.env('token'),
            'Content-Type': 'application/json'
        }
    })
})

// for goals
Cypress.Commands.add('sentRequestT2', (method, endpoint, payload) => {
    return allure.step(`Trying to send ${method} request to ${endpoint}`, () => {
        if (payload && Object.keys(payload).length > 0) {
            allure.attachment(`requestBody for ${method} ${endpoint}`, JSON.stringify(payload), 'application/json')
            cy.log(`Trying to send ${method} request to ${endpoint} with body ${JSON.stringify(payload)}`)
        } else {
            cy.log(`Trying to send ${method} request to ${endpoint} without body`)
        }
        return cy.request({
            method: method,
            url: endpoint,
            body: payload,
            failOnStatusCode: false,
            headers: {
                Authorization: Cypress.env('token2'),
                Accept: 'application/json'
            }
        }).then((resp) => {
            allure.attachment(`responseBody for ${method} ${endpoint}`, JSON.stringify(resp.body), 'application/json')
            return cy.wrap(resp)  // Use cy.wrap() to ensure the response is chained properly
        })
    })
})