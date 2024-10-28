import {faker} from "@faker-js/faker";
import * as allure from "allure-js-commons"

const goalsURL = '/team/9012430611/goal'

export const getGoals = () => {
    return allure.step('Get a list of Goals', () => {
        return cy.sentRequestT2('GET', goalsURL, null)
    })
}

export const createGoal = () => {
    return allure.step('Create Goal with random data', () => {
        return cy.fixture('createGoal.json').then((body) => {
            const randomColor = faker.color.rgb({format: 'hex', casing: 'lower'})
            const randomDueDate = faker.date.future().getTime()
            const randomName = faker.company.name()
            const randomDescription = faker.lorem.sentence()
            body.name = randomName
            body.description = randomDescription
            body.color = randomColor
            body.due_date = randomDueDate
            cy.wrap(randomColor).as('randomColor');
            cy.wrap(randomDueDate).as('randomDueDate');
            cy.wrap(randomName).as('randomGoalName');
            cy.wrap(randomDescription).as('randomGoalDescription');
            return cy.sentRequestT2('POST', goalsURL, body)
        });
    })
};

export const getGoal = (goal_id) => {
    return allure.step('Get Goal by ID', () => {
        return cy.sentRequestT2('GET', `/goal/${goal_id}`, null)
    })
}

export const updateGoal = (goal_id) => {
    return allure.step('Update Goal with random data by ID', () => {
        const randomName = faker.company.name()
        const randomDescription = faker.lorem.sentence()
        const newBody = {name: randomName, description: randomDescription}
        cy.wrap(randomName).as('updatedGoalName')
        cy.wrap(randomDescription).as('updatedGoalDescription')
        return cy.sentRequestT2('PUT', `/goal/${goal_id}`, newBody)
    })
}

export const deleteGoal = (goal_id) => {
    return allure.step('Delete Goal by ID', () => {
        return cy.sentRequestT2('DELETE', `/goal/${goal_id}`, null)
    })
}

export const createKeyResult = (goal_id) => {
    return allure.step('Create KeyResult with random name by ID', () => {
        let randomName = faker.string.sample({min: 5, max: 10})
        cy.wrap(randomName).as('keyResultName')
        return cy.fixture('createKeyResult.json').then((body) => {
            body.name = randomName
            return cy.sentRequestT2('POST', `/goal/${goal_id}/key_result`, body)
        })
    })
}

export const editKeyResult = (key_result_id) => {
    return allure.step('Update KeyResult with random name by ID', () => {
        let randomName = faker.string.sample({min: 5, max: 10})
        cy.wrap(randomName).as('newKeyResultName')
        const newBody = {name: randomName}
        return cy.sentRequestT2('PUT', `/key_result/${key_result_id}`, newBody)
    })
}

export const deleteKeyResult = (key_result_id) => {
    return allure.step('Delete KeyResult by ID', () => {
        return cy.sentRequestT2('DELETE', `/key_result/${key_result_id}`, null)
    })
}

