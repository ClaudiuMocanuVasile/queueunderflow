<template>

    <section class="h-100 gradient-custom-2">
        <div class="container py-5 h-100">

            <!-- Profile Container -->
            <div class="card">

                <div class="rounded-top text-white d-flex flex-row cover">
                    <div class="ms-4 mt-5 d-flex flex-column" style="width: 150px;">
                        <!-- Profile image -->
                        <img src="https://mir-s3-cdn-cf.behance.net/project_modules/max_1200/626fd8140423801.6241b91e24d9c.png"
                            alt="Generic placeholder image" class="img-fluid img-thumbnail mt-4 mb-2"
                            style="width: 150px; z-index: 1">

                        <!-- Edit profile button -->
                        <button type="button" class="btn btn-outline-dark" data-mdb-ripple-color="dark"
                            style="z-index: 1;">
                            Edit profile
                        </button>
                    </div>

                    <!-- Displayed name and username -->
                    <div class="ms-3" style="margin-top: 130px;">
                        <h5>Displayed Name</h5>
                        <p>@username</p>
                    </div>
                </div>

                <!-- Profile scores -->
                <div class="pt-4 pb-4 text-black" style="background-color: #f8f9fa;">
                    <div class="d-flex justify-content-end text-center py-1">
                        <div>
                            <p class="mb-1 h5" id="user_questionsCount">17</p>
                            <p class="small text-muted mb-0">Questions posted</p>
                        </div>
                        <div class="px-3">
                            <p class="mb-1 h5" id="user_answerCount">40</p>
                            <p class="small text-muted mb-0">Answers given</p>
                        </div>
                        <div>
                            <p class="mb-1 h5" id="user_BestAnswerCount">18</p>
                            <p class="small text-muted mb-0">Best answer</p>
                        </div>
                        <div class="px-4">
                            <p class="mb-1 h5" id="user_score">361</p>
                            <p class="small text-muted mb-0">Score</p>
                        </div>
                    </div>
                </div>

                <!-- Profile Pills -->
                <div class="px-5 py-5">
                    <!-- Pills navs -->
                    <ul class="nav nav-pills mb-3" id="ex1" role="tablist">
                        <li class="nav-item" role="presentation">
                            <a class="nav-link active" id="ex1-tab-1" data-bs-toggle="pill" href="#profile-info"
                                role="tab" aria-controls="profile_tab" aria-selected="true">About</a>
                        </li>
                        <li class="nav-item" role="presentation">
                            <a class="nav-link" id="ex1-tab-2" data-bs-toggle="pill" href="#questions-posted" role="tab"
                                aria-controls="questions-posted" aria-selected="false">Questions posted</a>
                        </li>
                        <li class="nav-item" role="presentation">
                            <a class="nav-link" id="ex1-tab-3" data-bs-toggle="pill" href="#answers-given" role="tab"
                                aria-controls="answers-given" aria-selected="false">Answers given</a>
                        </li>
                        <li class="nav-item" role="presentation">
                            <a class="nav-link" id="ex1-tab-3" data-bs-toggle="pill" href="#achievements" role="tab"
                                aria-controls="achievements" aria-selected="false">✦ Achievements ✦</a>
                        </li>
                    </ul>
                    <!-- Pills navs -->

                    <hr>

                    <!-- Pills content -->
                    <div class="tab-content" id="ex1-content">

                        <!-- About -->
                        <div class="tab-pane fade show active" id="profile-info" role="tabpanel"
                            aria-labelledby="profile-info">
                            <div class="card-body text-black">
                                <div class="py-2">
                                    <p class="font-italic mb-1" id="user_description"> [Aci campul "description" de la
                                        fiecare user]</p>
                                    <p class="font-italic mb-4 mt-4"><span style="color: blue">Birthday:</span>
                                        10/04/2000</p>
                                </div>
                            </div>
                        </div>

                        <!-- Questions posted -->
                        <div class="tab-pane fade" id="questions-posted" role="tabpanel"
                            aria-labelledby="questions-posted">

                            <div class="card mb-3">
                                
                                <!-- Pentru fiecare intrebare a userului din baza de date, se va insera template-ul asta *preferabil din JavaScript*-->
                                <!-- Question element exemplu 1-->
                                <div class="row mb-1">
                                    <!-- Image -->
                                    <div class="col-md-4">
                                        <img src="https://t4.ftcdn.net/jpg/01/57/24/19/360_F_157241916_H518BbbcbFavVTRCGjQsYOWGKrc4RGnZ.jpg"
                                            class="img-fluid rounded-start" alt="">
                                    </div>
                                    <!-- Question -->
                                    <div class="col-md-8">
                                        <div class="card-body">
                                            <h3 class="card-title mt-5 mb-4">Your question:</h3>
                                            <p class="card-text">Insert question description here... <br></p>
                                            <a class="card-text text-muted" href="#question_page">Go to question</a>
                                        </div>
                                    </div>
                                </div>
                                <!-- Question element exemplu 1 END -->

                                <!-- Question element exemplu 2 -->
                                <div class="row mb-1">
                                    <!-- Image -->
                                    <div class="col-md-4">
                                        <img src="https://t4.ftcdn.net/jpg/01/57/24/19/360_F_157241916_H518BbbcbFavVTRCGjQsYOWGKrc4RGnZ.jpg"
                                            class="img-fluid rounded-start" alt="">
                                    </div>
                                    <!-- Question -->
                                    <div class="col-md-8">
                                        <div class="card-body">
                                            <h3 class="card-title mt-5 mb-4">Your question:</h3>
                                            <p class="card-text"> <br> Hello here is another question. Can penguins fly?</p>
                                            <a class="card-text text-muted" href="#question_page">Go to question</a>
                                        </div>
                                    </div>
                                </div>
                                <!-- Question element exemplu 2 END -->

                            </div>

                        </div>

                        <!-- Answers given -->
                        <div class="tab-pane fade" id="answers-given" role="tabpanel" aria-labelledby="answers-given">

                            <div class="card mb-5">
                                
                                <!-- Pentru fiecare raspuns dat de user se va insera template-ul asta *preferabil din JavaScript*-->
                                <!-- Answer element exemplu 1-->
                                <div class="row mb-1">
                                    <!-- Image -->
                                    <div class="col-md-4 bg-light">
                                        <img src="https://cdn-icons-png.flaticon.com/512/1293/1293029.png"
                                            class="img-fluid w-50 h-80 rounded-start mx-auto d-block m-3" alt="">
                                    </div>
                                    <!-- Answer -->
                                    <div class="col-md-8 mb-5">
                                        <div class="card-body">
                                            <h3 class="card-title mt-5 mb-4">Question Title</h3>
                                            <p class="card-text">Insert user answer for this question here... <br></p>
                                            <p>✦ Upvotes: 5</p>
                                            <p>✦ Downvotes: 0</p>
                                            <a class="card-text text-muted mb-5" href="#question_page">See full page</a>
                                        </div>
                                    </div>
                                </div>
                                <!-- Answer element exemplu 1 END -->

                                <!-- Answer element exemplu 2 -->
                                <div class="row mb-1">
                                    <!-- Image -->
                                    <div class="col-md-4 bg-light">
                                        <img src="https://cdn-icons-png.flaticon.com/512/1293/1293029.png"
                                            class="img-fluid w-50 h-80 rounded-start mx-auto d-block m-3" alt="">
                                    </div>
                                    <!-- Answer -->
                                    <div class="col-md-8 mb-5">
                                        <div class="card-body">
                                            <h3 class="card-title mt-5 mb-4">What would you choose, Pepsi or Coca cola?</h3>
                                            <p class="card-text"> <br> Does it even matter? It's almost the same! But let's go with Pepsi</p>
                                            <p>✦ Upvotes: 3</p>
                                            <p>✦ Downvotes: 1</p>
                                            <a class="card-text text-muted" href="#question_page">See full page</a>
                                        </div>
                                    </div>
                                </div>
                                <!-- Answer element exemplu 2 END -->

                            </div>

                        </div>

                        <!-- Achievements -->
                        <div class="tab-pane fade" id="achievements" role="tabpanel" aria-labelledby="achievements">
                            achievements loading...
                        </div>

                    </div>
                    <!-- Pills content -->
                </div>
                <!-- Profile Pills end -->

            </div>
            <!-- Profile Container end -->
        </div>

    </section>

</template>

<script>
import axios from 'axios';

export default {
    name: 'ProfileView',
    components: {
    },
    methods: {

    },
}
</script>

<style>
.cover {
    /* background: linear-gradient(to right bottom, rgb(50, 36, 80), rgb(79, 69, 128), rgb(105, 94, 161)); */
    background: linear-gradient(to left bottom, rgb(28, 27, 29), rgb(56, 41, 90));
    height: 200px;
}

.gradient-custom-2 {
    /* fallback for old browsers */
    background: #fbc2eb;

    /* Chrome 10-25, Safari 5.1-6 */
    background: -webkit-linear-gradient(to right, rgba(251, 194, 235, 1), rgba(166, 193, 238, 1));

    /* W3C, IE 10+/ Edge, Firefox 16+, Chrome 26+, Opera 12+, Safari 7+ */
    background: linear-gradient(to right, rgb(194, 217, 251), rgb(185, 166, 238));
}
</style>
