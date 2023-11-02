const Slider = () => {
  const slideRef = document.createElement("div");
  const loadingProgress = 0;

  const handleClickNext = () => {
    let items = slideRef.querySelectorAll(".item");
    slideRef.appendChild(items[0]);
  };

  const handleClickPrev = () => {
    let items = slideRef.querySelectorAll(".item");
    slideRef.prepend(items[items.length - 1]);
  };

  const data = [
    {
      id: 1,
      imgUrl:
        "https://upload.wikimedia.org/wikipedia/commons/5/55/Parque_Bicentenario%2C_Vitacura%2C_Santiago_20200314_02.jpg",
      desc: "Some beautiful moons cannot be created without getting creativity.",
      name: "PARQUE BICENTENARIO",
    },
    {
      id: 2,
      imgUrl:
      "https://upload.wikimedia.org/wikipedia/commons/b/ba/Parque_Araucano_16.jpg",
      desc: "Some beautiful moons cannot be created without getting creativity.",
      name: "PARQUE ARAUCANO",
    },
    {
      id: 3,
      imgUrl:
        "https://media-front.elmostrador.cl/2020/08/A_UNO_1207849-scaled-1.jpg",
      desc: "Some beautiful moons cannot be created without getting creativity.",
      name: "PARQUE OHIGGINS",
    },
    {
      id: 4,
      imgUrl:
      
        "https://upload.wikimedia.org/wikipedia/commons/b/b7/Parque_In%C3%A9s_de_Su%C3%A1rez%2C_Santiago_de_Chile.jpg",
      desc: "Some beautiful moons cannot be created without getting creativity.",
      name: "PARQUE INÉS DE SUÁREZ",
    },
    {
      id: 5,
      imgUrl:
        "https://e8s3v3w7.rocketcdn.me/wp-content/uploads/2017/11/chile-santiago-mit-zahlreichen-attraktionen-bietet-der-riesige-parque-metropolitano-in-santiago-de-chile-sowohl-erholung-und-entspannung-als-auch-kultur-und-unterhaltung-byvalet-shutterstoc.jpg",
      desc: "Some beautiful moons cannot be created without getting creativity.",
      name: "PARQUE METROPOLITANO",
    },
    {
      id: 6,
      imgUrl:
        "https://www.munivina.cl/wp-content/uploads/2023/03/PARQUE-QUINTA-VERGARA-3-scaled.jpg",
      desc: "Some beautiful moons cannot be created without getting creativity.",
      name: "PARQUE QUINTA VERGARA",
    },
    {
      id: 7,
      imgUrl:
      "https://chileestuyo.cl/wp-content/uploads/2021/03/Laguna-Cuellar-scaled.jpg",
      desc: "Some beautiful moons cannot be created without getting creativity.",
      name: "CAJÓN DEL ACHIBUENO",
    },
  ];

  // create the contenedor div
  const container = document.createElement("div");
  container.classList.add("containerslider");

  //create the loadbar div
  const loadbar = document.createElement("div");
  loadbar.classList.add("loadbar");
  loadbar.style.width = `${loadingProgress}%`;

  //Append loadbar to contenedor
  container.appendChild(loadbar);

  //Append slide div to contenedor
  container.appendChild(slideRef);

  // Create and append items to slide div

  data.forEach((item) => {
    const slideItem = document.createElement("div");
    slideItem.classList.add("item");
    slideItem.style.backgroundImage = `url(${item.imgUrl})`;

    const content = document.createElement("div");
    content.classList.add("content");

    const name = document.createElement("div");
    name.classList.add("name");
    name.textContent = item.name;

    const des = document.createElement("div");
    des.classList.add("des");
    des.textContent = item.desc;

    const button = document.createElement("button");
    button.textContent = "See more";

    content.appendChild(name);
    content.appendChild(des);
    content.appendChild(button);
    slideItem.appendChild(content);
    slideRef.appendChild(slideItem);

    // Create the buttons div
    const buttons = document.createElement("div");
    buttons.classList.add("buttons");

    // Create the prev button
    const prevButton = document.createElement("button");
    prevButton.id = "prev";
    prevButton.addEventListener("click", handleClickPrev);

    const prevIcon = document.createElement("i");
    prevIcon.className = "fa fa-angle-left";
    prevButton.appendChild(prevIcon);


    // Create the next Button
    const nextButton = document.createElement("button");
    nextButton.id = "next";
    nextButton.addEventListener("click", handleClickNext);

    const nextIcon =  document.createElement("i");
    nextIcon.className ="fa fa-angle-right";
    nextButton.appendChild(nextIcon);

    // Append buttons to the contenedor
    buttons.appendChild(prevButton)
    buttons.appendChild(nextButton)
    container.appendChild(buttons);
  });

  // Add the contenedor to the DOM (assuming there is an element with id "root" where you want to mount the slider)
  document.getElementById("root").appendChild(container);
};

// Call the Slider function to initialize the slider
Slider();
