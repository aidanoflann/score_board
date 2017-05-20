node() {
    git url: "https://github.com/aidanoflann/score_board", credentialsId: 'dc61f703-7780-457a-a44e-9b58dac6aab7'
    sh "git rev-parse HEAD > .git/commit-id"
    def commit_id = readFile('.git/commit-id').trim()
    println commit_id

    stage "build"
    sh "docker build . -t score_board"

    stage "publish"
    sh "DOCKER_COMMAND=\$(aws ecr get-login)"
    sh "\$DOCKER_COMMAND"
    sh "docker tag score_board 364843010988.dkr.ecr.eu-west-1.amazonaws.com/score_board"
    sh "docker push 364843010988.dkr.ecr.eu-west-1.amazonaws.com/score_board"
}
