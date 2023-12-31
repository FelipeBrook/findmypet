const Slider = () => {
  const slideRef = document.createElement("div");
  const loadingProgress = 0;

  const handleClickNext = () => {
    let items = slideRef.querySelectorAll(".itemslider");
    slideRef.appendChild(items[0]);
  };

  const handleClickPrev = () => {
    let items = slideRef.querySelectorAll(".itemslider");
    slideRef.prepend(items[items.length - 1]);
  };

  const data = [
    {
      id: 1,
      imgUrl:
        "https://upload.wikimedia.org/wikipedia/commons/5/55/Parque_Bicentenario%2C_Vitacura%2C_Santiago_20200314_02.jpg",
      desc: "",
      name: "PARQUE BICENTENARIO",
    },
    {
      id: 2,
      imgUrl:
        "https://upload.wikimedia.org/wikipedia/commons/b/ba/Parque_Araucano_16.jpg",
      desc: "El Parque Araucano, ubicado en la comuna de Las Condes en Santiago de Chile, es un excelente lugar para pasear con tu perro. Con sus 22 hectáreas aproximadamente, el parque ofrece amplias áreas verdes y una variedad de actividades que puedes disfrutar en familia o individualmente",
      name: "PARQUE ARAUCANO",
    },
    {
      id: 3,
      imgUrl:
        "https://media-front.elmostrador.cl/2020/08/A_UNO_1207849-scaled-1.jpg",
      desc: ".",
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
        "https://traveler.marriott.com/es/wp-content/uploads/sites/2/2018/12/GI-642414680-San_Cristobal_Cable_Car-header.jpg",
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
    slideItem.classList.add("itemslider");
    slideItem.style.backgroundImage = `url(${item.imgUrl})`;

    const content = document.createElement("div");
    content.classList.add("contentslider");

    const name = document.createElement("div");
    name.classList.add("nameslider");
    name.textContent = item.name;

    const des = document.createElement("div");
    des.classList.add("desslider");
    des.textContent = item.desc;

    const button = document.createElement("button");
    button.textContent = "Ver más";

    content.appendChild(name);
    content.appendChild(des);
    content.appendChild(button);
    slideItem.appendChild(content);
    slideRef.appendChild(slideItem);

    // Create the buttons div
    const buttons = document.createElement("div");
    buttons.classList.add("buttonsslider");

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

    const nextIcon = document.createElement("i");
    nextIcon.className = "fa fa-angle-right";
    nextButton.appendChild(nextIcon);

    // Append buttons to the contenedor
    buttons.appendChild(prevButton);
    buttons.appendChild(nextButton);
    container.appendChild(buttons);
  });

  // Add the contenedor to the DOM (assuming there is an element with id "root" where you want to mount the slider)
  document.getElementById("root").appendChild(container);
};

// Call the Slider function to initialize the slider
Slider();
