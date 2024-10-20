const {getFolders, createFolder, updateFolder, deleteFolder} = require("../../utils/foldersMethods");

describe('check folders functionality on clickup', () => {
    it('get folders', () => {
        getFolders().then((response) => {
            expect(response.status).to.eq(200)
        })
    })

    it('create folder', () => {
        createFolder().then((response) => {
            expect(response.status).to.eq(200)
        })
    })

    it('update folder', () => {
        createFolder().then((response) => {
            const id = response.body.id
            updateFolder(id).then((response) => {
                expect(response.status).to.eq(200)
            })
        })
    })

    it('delete folder', () => {
        createFolder().then((response) => {
            const id = response.body.id
            deleteFolder(id)
                .then((response) => {
                    cy.log(response.status)
                    expect(response.status).to.eq(200)
                })
        })
    })
})
