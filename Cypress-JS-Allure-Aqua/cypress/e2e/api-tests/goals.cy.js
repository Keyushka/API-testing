const {
    getGoals, createGoal, getGoal, updateGoal, deleteGoal,
    createKeyResult, editKeyResult, deleteKeyResult
} = require("../../utils/goalsMethods");

describe('Check goals functionality on clickup', () => {

    it('Get Goals', () => {
        getGoals().then((response) => {
            expect(response.status).to.eq(200)
        })
    })

    it('Create Goal', () => {
        createGoal().then((response) => {
            expect(response.status).to.eq(200)
        })
    })

    it('Get Goal', () => {
        createGoal().then((createResponse) => {
            const goal_id = createResponse.body.goal.id
            getGoal(goal_id).then((getResponse) => {
                const goal = getResponse.body.goal
                expect(getResponse.status).to.eq(200)
                cy.get('@randomColor').then((color) => {
                    expect(goal.color).to.eq(color)
                })
                cy.get('@randomDueDate').then((dueDate) => {
                    expect(goal.due_date).to.eq(dueDate.toString())
                })
                cy.get('@randomGoalName').then((name) => {
                    expect(goal.name).to.eq(name)
                })
                cy.get('@randomGoalDescription').then((description) => {
                    expect(goal.description).to.eq(description)
                })
            })
        })
    })

    it('Update Goal', () => {
        createGoal().then((createResponse) => {
            const goal_id = createResponse.body.goal.id
            updateGoal(goal_id).then((updateResponse) => {
                expect(updateResponse.status).to.eq(200)
                getGoal(goal_id).then((getResponse) => {
                    const updatedGoal = getResponse.body.goal
                    expect(getResponse.status).to.eq(200)
                    cy.get('@updatedGoalName').then((name) => {
                        expect(updatedGoal.name).to.eq(name)
                    })
                    cy.get('@updatedGoalDescription').then((description) => {
                        expect(updatedGoal.description).to.eq(description)
                    })
                })
            })
        })
    })

    it('Delete Goal', () => {
        createGoal().then((response) => {
            const goal_id = response.body.goal.id
            deleteGoal(goal_id).then((response) => {
                expect(response.status).to.eq(200)
                getGoal(goal_id).then((response) => {
                    expect(response.status).to.be.oneOf([404, 403])
                    // чомусь в постмані видає 404, а тут часто - 403
                })
            })
        })
    })

    it('Create Key Result', () => {
        createGoal().then((goalResponse) => {
            const goal_id = goalResponse.body.goal.id
            createKeyResult(goal_id).then((keyResultResponse) => {
                expect(keyResultResponse.status).to.eq(200)
                getGoal(goal_id).then((response) => {
                    const keyResultId = keyResultResponse.body.key_result.id
                    const goal = response.body.goal
                    expect(response.status).to.eq(200)
                    expect(goal).to.have.property('key_results')
                    const keyResult = goal.key_results.find(result => result.id === keyResultId)
                    expect(keyResult).to.not.be.undefined
                    cy.get('@keyResultName').then((name) => {
                        expect(keyResult.name).to.eq(name)
                    })
                })
            })
        })
    })

    it('Edit Key Result', () => {
        createGoal().then((goalResponse) => {
            const goal_id = goalResponse.body.goal.id
            createKeyResult(goal_id).then((keyResultResponse) => {
                expect(keyResultResponse.status).to.eq(200)
                const key_result_id = keyResultResponse.body.key_result.id
                editKeyResult(key_result_id).then((editResponse) => {
                    expect(editResponse.status).to.eq(200)
                    cy.get('@newKeyResultName').then((newName) => {
                        cy.get('@keyResultName').then((oldName) => {
                            expect(newName).to.not.eq(oldName)
                            getGoal(goal_id).then((goalResponse) => {
                                const updatedKeyResult = goalResponse.body.goal.key_results.find(
                                    (kr) => kr.id === key_result_id
                                )
                                expect(updatedKeyResult).to.exist
                                expect(updatedKeyResult.name).to.eq(newName)
                            })
                        })
                    })
                })
            })
        })
    })

    it('Delete Key Result', () => {
        createGoal().then((response) => {
            const goal_id = response.body.goal.id
            createKeyResult(goal_id).then((keyResultResponse) => {
                const key_result_id = keyResultResponse.body.key_result.id
                deleteKeyResult(key_result_id).then((deleteResponse) => {
                    expect(deleteResponse.status).to.eq(200)
                    getGoal(goal_id).then((goalResponse) => {
                        const deletedKeyResult = goalResponse.body.goal.key_results.find(
                            (kr) => kr.id === key_result_id
                        )
                        expect(deletedKeyResult).to.be.undefined
                    })
                })
            })
        })
    })

})