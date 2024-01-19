let data = [
  {
    year: 2024,
    events: [
      {
        title: "📜 AWS Certified Associate SysOps",
        subtitle: "@AWS",
        body: "Passed my AWS Associate DevOps .",
        date: {
          day: "1",
          month: "Apr"
        }
      },
      {
        title: "Started a Masters",
        subtitle: "@Univeristy of Hull",
        body: "Started a MSc in Artificial Intelligence.",
        date: {
          day: "1",
          month: "May"
        }
      },
    ]
  },
  {
    year: 2023,
    events: [
      {
        title: "🎓 BSc Computer Science ",
        subtitle: "@Univeristy of London",
        body: "After 4 years, a pandemic, a house move, and countless nights in the library, I finished my degree. Onto new adventures!",
        date: {
          day: "1",
          month: "Jun"
        }
      },
    ]
  },
  {
    year: 2022,
    events: [
      {
        title: "🚗 Driving license B",
        subtitle: "@Driving School",
        body: "2/2/22 - on this date I passed my driving test with one minor.",
        date: {
          day: "22",
          month: "Feb"
        }
      },
    ]
  },
  {
    year: 2020,
    events: [
      {
        title: "💼 Software Support",
        subtitle: "@Radancy",
        body: "Responsible for providing support CMS support to clients. Liaise with third parties to complete system integrations (mainly ATS and Analytics). Perform website updates through the CMS admin area and conduct QA and UAT tasks. Manage support tickets through JIRA.",
        date: {
          day: "1",
          month: "Aug"
        }
      },
    ]
  },
  {
    year: 2019,
    events: [
      {
        title: "💼 Software Support",
        subtitle: "@Crownpeak",
        body: "Responsible for providing support on the Accessibility checker (called DQM). Monitor JIRA support queue and escalate issues. Contributed to the API documentation and built an internal reporting tool using Python.",
        date: {
          day: "1",
          month: "Apr"
        }
      },
      {
        title: "Started a Degree",
        subtitle: "@University of London",
        body: "Started my first degree in Computer Science at the Birkbeck, University of London.",
        date: {
          day: "1",
          month: "Oct"
        }
      }
    ]
  },
  {
    year: 2018,
    events: []
  },
  {
    year: 2017,
    events: [{
      title: "💼 Software Support",
      subtitle: "@Actionstep UK",
      body: "Responsible for providing support on the Legal Case Management System provided. Conduct demos of the platform and setup new client integrations with third parties (Xero, NetDocs, Google Drive). Monitor JIRA support queue and escalate issues.",
      date: {
        day: "1",
        month: "Apr"
      }
    }]
  },
  {
    year: 2016,
    events: []
  },
  {
    year: 2015,
    events: [{
      title: "💼 Account Manager",
      subtitle: "@FlatClub",
      body: "Responsible for helping cohorts of employees get their first accommodation in the UK through the service platform. Overlooked big accounts such as Google and Vodafone new employees. Received a mention by Vodafone for outstanding assistance.",
      date: {
        day: "1",
        month: "Apr"
      }
    }]
  },
  {
    year: 2014,
    events: [
      {
        title: "🛫 Moved to London",
        subtitle: "",
        body: "At the age of 19 I decided to move from Lisbon to London.",
        date: {
          day: "17",
          month: "Sep",
          year: "2014"
        }
      },
      {
        title: "💼 Coffee Barista",
        subtitle: "@AMT",
        body: "At this time I was living in a hostel in central London, called The Clink 78, where I made a few friends. \
        I started working in a coffee shop inside King's Cross station as coffee barista.",
        date: {
          day: "1",
          month: "Dec"
        }
      }
    ]
  }
];

function htmlBuilder (entry){ 
  let html = `
    <div class="uia-timeline__annual-sections" >
      <span class="uia-timeline__year" aria-hidden="true">${entry.year}</span>
      <div class="uia-timeline__groups">`;
  
  entry.events.forEach(e => {
    html += `
    <section class="uia-timeline__group" aria-labelledby="timeline-demo-1-heading-1">
      <div class="uia-timeline__point uia-card" data-uia-card-skin="1" data-uia-card-mod="1">
        <div class="uia-card__container">
          <div class="uia-card__intro">
            <div>
              <h3 id="timeline-demo-1-heading-1" class="ra-heading">${e.title}</h3>
              <p class="text-muted">${e.subtitle}</p>
            </div>
            <span class="uia-card__time">
              <time>
                <span class="uia-card__day">${e.date.day}</span>
                <span>${e.date.month}</span>
              </time>
            </span>
          </div>
          <div class="uia-card__body">
            <div class="uia-card__description">
              <p>${e.body}</p>
            </div>
          </div>
        </div>
      </div>
    </section>`  
  });
  
  html += '</div>';

  return html;
};

data.forEach(e => document.querySelector('#annual_sections').innerHTML += htmlBuilder(e));
  