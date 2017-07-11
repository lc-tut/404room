Rails.application.routes.draw do
  get 'api/log' => 'api#show'

  post 'api/log' => 'api#create'

  get 'test/index'

  # For details on the DSL available within this file, see http://guides.rubyonrails.org/routing.html
end
