import tensorflow as tf
import numpy as np
import collections
import sys
import os


#redefine the layer  of tf.keras.models module
Model = tf.keras.models.Model
Dense = tf.keras.layers.Dense
LSTM  = tf.keras.layers.LSTM
GRU = tf.keras.layers.GRU
RepeatVector = tf.keras.layers.RepeatVector
Flatten = tf.keras.layers.Flatten
Embedding = tf.keras.layers.Embedding
Plot_model = tf.keras.utils.plot_model



class basic(object):
  """
   the main function of class is to get the relationshaip between layers from adjacency matrix
   
   Examples :
    >>> x = np.array([[0, 1, 1, 1, 1, 1],
    >>>             [0, 0, 1, 1, 1, 1],
    >>>             [0, 0, 0, 1, 1, 1],
    >>>             [0, 0, 0, 0, 1, 1],
    >>>             [0, 0, 0, 0, 0, 1],
    >>>             [0, 0, 0, 0, 0, 0]], np.int32)
    >>> y = {'a': {'Dense': 3}, 'b': {'LSTM': 4}, 'c': {'Dense': 5}, 'd': {'GRU': 6}, 'e': {'Dense': 7},'f': {'LSTM': 8}}
    >>> model=basic()
    >>> print(model.get_releation_layers(x,y))
  """
  
  def __init__(self):
    super(basic, self).__init__()

  def get_releation_layers(self,input,layers):
    """
    this function can get the relationshaip between layers from adjacency matrix
    
    :param input: adjacency matrix
    :param layers: node information
    :return: the relationshaip between layers
    """
    
    assert type(input)==np.ndarray
    y_index = np.array(list(layers))
    releation = collections.OrderedDict()
    for i in range(1, len(input)):
      coord_y = None
      temp_list = []
      for j in range(i):
        if input[j][i] == 1:
          input[i][i] += input[j][i]
          coord_x = [y_index[z] for z in range(len(y_index)) for z in range(len(y_index)) if z == j][0]
          coord_y = [y_index[z] for z in range(len(y_index)) for z in range(len(y_index)) if z == i][0]
          temp_list.append("%s" % coord_x)
          
      if coord_y!=None:
        releation["%s" % (coord_y)] = temp_list
    if len(releation)==0:
      return None
    return releation


class rnn_net(basic):
  """

  :param basic: inherit from class basic
  
  Examples :
    >>> x = np.array([[0, 1, 1, 1, 1, 1],
    >>>             [0, 0, 1, 1, 1, 1],
    >>>             [0, 0, 0, 1, 1, 1],
    >>>             [0, 0, 0, 0, 1, 1],
    >>>             [0, 0, 0, 0, 0, 1],
    >>>             [0, 0, 0, 0, 0, 0]], np.int32)
    >>> y = {'a': {'Dense': 3}, 'b': {'LSTM': 4}, 'c': {'Dense': 5}, 'd': {'GRU': 6}, 'e': {'Dense': 7},'f': {'LSTM': 8}}
    >>> model=rnn_net(x, y)
    >>> print(model.releation)
    >>> input,output=model.getlayers()
    >>> net= Model(inputs=[input],outputs=[output])
    >>> net.summary()
    >>> Plot_model(net,show_shapes=True)

  """
  
  def __init__(self,graph,layers):
    """
    
    :param graph: adjacency matrix between layers
    :param layers: node imformations
    """
    super(rnn_net, self).__init__()
    self.releation=self.get_releation_layers(graph,layers)
  
    self.input_layers=layers
    self.inputshape = tf.keras.Input(shape=(10,))
    
  def nametolayers(self,index,input):
    """
    this function  can get layers from the releateship of adjacency
    
    :param index: node name
    :param input: the shape of current layer
    :return: layers of tensorflow
    """
    layer=None
    
    if list(self.input_layers[index])[0] =='Dense':
      layer=Dense(list(self.input_layers[index].values())[0][0])
      
    elif list(self.input_layers[index])[0] =='LSTM':
      
      if len(input.shape)==2:
        input=Embedding(output_dim=512, input_dim=100, input_length=input.shape[1])(input)
        layer=LSTM(list(self.input_layers[index].values())[0][0],return_sequences=list(self.input_layers[index].values())[0][1])

      elif len(input.shape)==3:
        layer=LSTM(list(self.input_layers[index].values())[0][0],return_sequences=list(self.input_layers[index].values())[0][1])
        
      else :
        print("\033[41;36m error in %s in %s line\n \033[0m" % (os.path.basename(sys.argv[0]), sys._getframe().f_lineno))
        print("Error massage: the input shape of node %s is mistake!\n\n"%(index))
  
    elif list(self.input_layers[index])[0] =='GRU':
      
      if len(input.shape) == 2:
        input = Embedding(output_dim=512, input_dim=100, input_length=input.shape[1])(input)
        layer = GRU(list(self.input_layers[index].values())[0][0],
                     return_sequences=list(self.input_layers[index].values())[0][1])
  
      elif len(input.shape) == 3:
        layer = GRU(list(self.input_layers[index].values())[0][0],
                     return_sequences=list(self.input_layers[index].values())[0][1])
        
      else:
        print("\033[41;36m error in %s in %s line\n \033[0m" % (os.path.basename(sys.argv[0]), sys._getframe().f_lineno))
        print("Error massage: the input shape of node %s is mistake!\n\n" % (index))
    
    if layer ==None:
      return None
    else:
      return layer(input)
  
  def getlayers(self):
    """
    this function can obtain model from both adjacency matrix and node information
    
    :return: model of tensorflow
    """
    m_layers=collections.OrderedDict()
    
    m_layers['a']=self.nametolayers('a',self.inputshape)
    
    y_index = np.array(list(self.input_layers))
    
    if self.releation!=None:
      for index, value in self.releation.items():
        temp_layer = []
        for j in range(len(y_index)):
          
          if value[0] == y_index[j]:
            temp_layer.append(m_layers[value[0]])
            
        if len(value) > 1:
          for layer in range(1, len(value)):
            for j in range(len(y_index)):
              if value[layer] == y_index[j]:
                temp_layer.append(m_layers[value[layer]])

        ## concatenate layer
        output = temp_layer[0]
        if len(temp_layer) > 1:
         
          for layer_index in range(1,len(temp_layer)):
            if temp_layer[layer_index]==None and len(temp_layer[0].shape)!=len(temp_layer[layer_index].shape):
              print("\033[41;36m error in %s in %s line\n \033[0m" % (
                os.path.basename(sys.argv[0]), sys._getframe().f_lineno))
              print("Error massage: the concatenate of node %s error!\n\n" % (layer_index))
          
          output = tf.keras.layers.concatenate([layer for layer in temp_layer])
  
        output=self.nametolayers(index,output)
        m_layers[index]=output
      
      return self.inputshape, output
    else:
      return None,None
    
  def baselines(self, input_dim, output_dim):
    """
    this function can provide a standard model to forrcast wind energy
    
    
    :param input_dim: the shape of model input
    :param output_dim: the shape of model output
    :return: model of tensorflow
    """
    out=Dense(64, input_dim=input_dim)(self.inputshape)
    out=RepeatVector(6)(out)
    out=LSTM(256, return_sequences=True)(out)
    out=LSTM(32)(out)
    output=Dense(output_dim)(out)
    return self.inputshape,output





if __name__=="__main__":

  
  # x = np.array([[0, 1, 1, 0, 0, 0],
  #               [0, 0, 1, 0, 0, 0],
  #               [0, 0, 0, 0, 0, 0],
  #               [0, 0, 0, 0, 0, 0],
  #               [0, 0, 0, 0, 0, 0],
  #               [0, 0, 0, 0, 0, 0]], np.int32)
  # y = {'a':{'LSTM': [4,True]}, 'b': {'Dense': [5]}, 'c':{'LSTM': [4,False]}, 'd': {'GRU':[6,False] }, 'e': {'Dense': [7]},'f': {'LSTM': [8,False]}}
  #
 
  x = np.array([[0, 1, 1, 1, 1, 1],
                [0, 0, 1, 1, 1, 1],
                [0, 0, 0, 1, 1, 1],
                [0, 0, 0, 0, 1, 1],
                [0, 0, 0, 0, 0, 1],
                [0, 0, 0, 0, 0, 0]], np.int32)
  # x=np.zeros((6,6))
  # y = {'a': {'Dense': [7]}, 'b': {'Dense': [5]}, 'c': {'LSTM': [4, False]}, 'd': {'GRU': [6,False]},
  #      'e': {'LSTM': [4, False]}, 'f': {'LSTM': [8,False]}}
  y = {'a': {'LSTM': [4, True]}, 'b':{'LSTM': [13, True]}, 'c': {'LSTM': [4, True]}, 'd': {'GRU': [3, True]},
       'e': {'LSTM': [12, True]}, 'f': {'LSTM': [8, False]}}


  model=rnn_net(x, y)
  print(model.releation)
  input,output=model.getlayers()
  if input!= None:
    net= Model(inputs=[input],outputs=[output])
    net.summary()
    Plot_model(net,show_shapes=True)
  else :
    print("model was not created!")
  


