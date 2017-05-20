node() {
    docker.withRegistry('http://364843010988.dkr.ecr.eu-west-1.amazonaws.com', '76f4ee9e-e579-407d-b3c0-b03b537581db') {

        git url: "https://github.com/aidanoflann/score_board", credentialsId: 'dc61f703-7780-457a-a44e-9b58dac6aab7'
        sh "git rev-parse HEAD > .git/commit-id"
        def commit_id = readFile('.git/commit-id').trim()
        println commit_id

        stage "docker_login"
        sh "DOCKER_COMMAND=${aws ecr get-login}"
        sh "$DOCKER_COMMAND"

        stage "build"
        def app = docker.build "score_board"

        stage "publish"
        app.push 'master'
        app.push "${commit_id}"
    }
}
