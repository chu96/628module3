library(shiny)
library(leaflet)

data=read.csv("data/merged.csv")
city=as.character(unique(data$city))
data$weekday_close_after_23=1-data$weekday_close_after_23
data$weekend_close_after_23=1-data$weekend_close_after_23

m=lm(star~as.factor(BusinessParking)+as.factor(tvslabel)+as.factor(caterslabel)+as.factor(outdoorlabel)+
       as.factor(grouplabel)+as.factor(wheellabel)+as.factor(reservelabel) +as.factor(takeoutlabel)+
       as.factor(cardlabel)+as.factor(wifilabel)+as.factor(bikelabel)+as.factor(delilabel)+
       
       
       as.factor(weekday_close_after_23)+as.factor(weekend_close_after_23)+as.factor(weekend_hour_g11)+
       
       as.factor(RestaurantsPriceRange2)+ as.factor(noiselabel)+as.factor(city),data)


predictor=c("BusinessParking","tvslabel","caterslabel","outdoorlabel","grouplabel","wheellabel","reservelabel","takeoutlabel",
                  "cardlabel","wifilabel","bikelabel","delilabel",
                  "weekday_close_after_23","weekend_close_after_23","weekend_hour_g11",
                  "RestaurantsPriceRange2","noiselabel","city")

ui <- fluidPage(
  titlePanel("Ice Cream Yelp Ratings in USA"),
  
  tabsetPanel(
    tabPanel("General Summary",
             sidebarPanel(
               selectInput(inputId="city",
                           label="City:",
                           choices=c('None',city)),
               conditionalPanel("input.city != 'None'",
                                selectInput(inputId="single",
                                            label="Aspect you concern about:",
                                            choices=c('None','Flavor','Property','Service')),
                                actionButton("rec","Recommendation",icon("refresh")),
                                tableOutput(outputId="recommand"))),
             mainPanel(imageOutput(outputId="usa"))
             ),
    
    tabPanel("Ratings Prediction & Suggestion",
             sidebarPanel(
               titlePanel("Available services"),
               checkboxInput(inputId=predictor[1],
                             label="Parking"),
               checkboxInput(inputId=predictor[2],
                             label="TV"),
               checkboxInput(inputId=predictor[3],
                             label="Caters"),
               checkboxInput(inputId=predictor[4],
                             label="Outdoor seats"),
               checkboxInput(inputId=predictor[5],
                             label="Good for groups"),
               checkboxInput(inputId=predictor[6],
                             label="Wheels friendly"),
               checkboxInput(inputId=predictor[7],
                             label="Reservation"),
               checkboxInput(inputId=predictor[8],
                             label="Take out"),
               checkboxInput(inputId=predictor[9],
                             label="Card acceptable"),
               checkboxInput(inputId=predictor[10],
                             label="Wifi"),
               checkboxInput(inputId=predictor[11],
                             label="Bike"),
               checkboxInput(inputId=predictor[12],
                             label="Delivery"),
               titlePanel("Open time"),
               checkboxInput(inputId=predictor[13],
                             label="Close after 23:00 on weekdays"),
               checkboxInput(inputId=predictor[14],
                             label="Close after 23:00 on weekends"),
               checkboxInput(inputId=predictor[15],
                             label="Open hours is greater than 11h on weekends")),
             sidebarPanel(
               radioButtons(inputId='price',
                            label='Price Range',
                            choiceNames=c("$","$$","$$$","$$$$"),
                            choiceValues=c(1,2,2,2),
                            inline=T),
               radioButtons(inputId='noise',
                            label='Noise level',
                            choiceNames=c("Noisy","Average","Quiet"),
                            choiceValues=1:3,
                            inline=T),
               selectInput(inputId="county",
                           label="Which city:",
                           choices=c("Charlotte","Cleveland","Las Vegas","Madison","Phoenix","Pittsburgh")),
               actionButton("go","Go!")),
             mainPanel(
               titlePanel("Predicted rating & Suggestions"),
               verbatimTextOutput("conclusion"))
             ),
    tabPanel("Contact",
             p("If you have any problems, please contact us."),
             p("Ke Chen: kchen323@wisc.edu"),
             p("Chen Hu: chu96@wisc.edu"),
             p("Nan Yan: nyan5@wisc.edu"),
             p("Richard Yang: gyang79@wisc.edu"))
  )
)

server <- function(input, output, session) {
  output$usa=renderImage({
    if(input$city=='None'){
      return(list(src = "image/usa.png",alt = "Face",width="815px",height="384px"))
      }else if(input$single == 'None'){
      return(list(
        src = paste('image/',input$city,'.png',sep=""),alt = "Face",width="1205.5px",height="275px"))
      }else{
        return(list(
          src = paste('image/',input$single,'/',input$city,'.png',sep=""),alt = "Face",width="500px",height="333px"))
        }
    },deleteFile=F)
  rec = eventReactive(input$rec,{
    if(input$city == "Las Vegas"){
      tab=as.data.frame(c("Snow Vegas Shave Ice","D-Scoops & Sweets Art of Flavor",
                                 "Cloud Tea","Froggies Snow Cone Shack",
                                 "Bubble Shave Ice","The Sugar Cookie","Frost N' Roll",
                                 "luff Ice","Super Swirl Frozen Yogurt & Boba Teas"))
    }else if(input$city == "Phoenix"){
      tab=as.data.frame(c("Novel Ice Cream","Raspados Solaris","Jacked Ice","Raspados Imperial","Brimley's Water & Ice,Desert Snow,The Water Connection"))
    }else if(input$city == "Cleveland"){
      tab=as.data.frame(c("Mitchell's Homemade Ice Cream-Cleveland","Honey Hut Ice Cream Shoppe","Honey Hut Ice Cream","Kamm's Corners Ice Cream Company"))
    }else if(input$city == "Charlotte"){
      tab=as.data.frame(c("Kona Snow","Ice Shavers"))
    }else if(input$city == "Pittsburgh"){
      tab=as.data.frame(c("Stickler's Ice Pops,FRIO Creamery","Antney's"))
    }else if(input$city == "Madison"){
      tab=as.data.frame(c("La Michoacana"))
    }
    colnames(tab)=input$city
    print(tab)
  })
  output$recommand=renderTable({rec()})
  
  
  score=eventReactive(input$go,
                      {
                        data.new=c(as.numeric(c(input$BusinessParking,input$tvslabel,input$caterslabel,input$outdoorlabel,input$grouplabel,
                                   input$wheellabel,input$reservelabel,input$takeoutlabel,input$cardlabel,input$wifilabel,
                                   input$bikelabel,input$delilabel,input$weekday_close_after_23,input$weekend_close_after_23,
                                   input$weekend_hour_g11)),input$price,input$noise,input$county)
                        data.new=as.data.frame(matrix(data.new,ncol=18))
                        colnames(data.new)=predictor
                        star=round(predict(m,data.new),digits=1)
                        print(paste("Your ice-cream shop may get",star,"points on Yelp.",sep=" "))
                        })
  output$conclusion=renderText({print(score())})
 
}

shinyApp(ui,server)

